"""The device command"""
from iothub.commands.device_commands import RetrieveMessagesTest
from iothub.commands.Strings import *
import re
from .Base import Base
import pem


def build_connect_string(host_name, device_id, access_key):
    """
        Build connection string based on values received
        Connection strings without RSA takes the following format:

        HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>

        :param host_name: Host Name of IoT Hub
        :param device_id: Device ID of particular device you want to interact with
        :param access_key: Access Key for device referenced above.
        :return: valid connection string
    """
    print("Building connection string")

    # Todo: 1) check if semi-colons are already at the end of each item passed in
    #       1a) If not, add them
    # Todo: 2) check if ending string "azure-devices.net" is already at the end of host_name
    #       2a) If not, append that to the end
    return '%s%s%s%s%s%s%s%s' % (
        HOST_NAME_STR, host_name, ';', DEVICE_ID_STR, device_id, ';', SHARED_ACCESS_KEY_STR, access_key)


def build_rsa_connect_string(host_name, device_id):
    """
        HostName=<host_name>;DeviceId=<device_id>;x509=true

        :param host_name: Host Name of IoT Hub
        :param device_id: Device ID of particular device you want to interact with.
        :return:
    """
    print("Building RSA Connection String")
    return "%s%s%s%s%s%s%s" % (HOST_NAME_STR, host_name, ';', DEVICE_ID_STR, device_id, ';', X509_STR)


def validate_connection_string(connect_string):
    """
        Validate connection string received from user
        Connection strings can take the following formats:

        1) HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
            a) Use this connection string if you are connecting straight to device
                without the use of RSA Certs/Keys

        2) HostName=<host_name>;DeviceId=<device_id>;x509=true
            a) Use this Connection string if accompanied with valid keys and
                certificates

        Regex to check if it's a valid connection string (Note, does not actually ping or check.
        It's simply telling whether it's valid based on input.  These values could be anything.

        (HOST_NAME_STR).*(DEVICE_ID_STR).*((x509_STR)|(SHARED_ACCESS_KEY_STR))

        :return: True if it is a valid connection string
    """
    print("Checking provided connection string")
    if re.match(REGEX_X509_STRING, connect_string):
        print("Valid x509 connection string...")
        return CONNECT_STRING_AND_RSA_CODE
    elif re.match(REGEX_CONNECT_STRING, connect_string):
        print("Valid access key connection string...")
        return CONNECT_STRING_CODE
    else:
        print("Invalid Connection String")
        return None


def validate_rsa_cert(rsa_cert_file):
    """
    Verify that the RSA Certificate File is in our specific format
    :param rsa_cert_file:
    :return: contents of certificate file
    """
    print("Validating RSA Certificate: ")
    if check_rsa_file(rsa_cert_file, CERTIFICATE_FILE_HEADER):
        return pem.parse_file(rsa_cert_file)
    else:
        return None


def validate_rsa_key(rsa_key_file):
    """
    Verify that the RSA Ke file is in our specific format
    :param rsa_key_file:
    :return: contents of key file
    """
    print("Validating RSA Key: ")
    if check_rsa_file(rsa_key_file, KEY_FILE_HEADER):
        return pem.parse_file(rsa_key_file)
    else:
        return None


def check_rsa_file(file, file_header):
    """
    Check the files as they are passed in.
    :param file: File that we are checking
    :param file_header: Header information that we are looking for
    :return: True or False on whether it is the file type we need and in the correct format
    """

    if file_header in open(file).read():
        print("%s is the correct type of file" % file)
        return True
    else:
        print("%s file not formatted correctly." % file)
        return False


class Device(Base):
    """Handles Device messages as they are received"""

    def run(self):
        if 'receive' in self.options and self.options["receive"]:
            # If receive, parse the self options to determine exact parameters
            self.parse_receive()

        else:
            print("seems like somethings messed up!")

    def parse_receive(self):
        """
        Parse values received to craft appropriate retrieval message for IoT Hub

        The following values are required for a connection:
        1) Connection String
            a) Host Name
            b) Device ID
            c) SharedAccess Key Or x509=true(certificate based connection)

        2) Transfer Protocol
            a) AMQP(Port 5671 or 443
            b) MQTT (Port 8883 or 443)
            c) HTTPS (Port 443)

        3) RSA Connection Certs (if connecting using certificates)
            a) RSA Certificate
            b) RSA Key
        """

        # Check Connection String
        connect_string = self.options[CONNECTION_STRING]
        connect_code = None

        # Check if user is attempting to connect with connection string
        if (self.options[CONNECT_SHORT] or self.options[CONNECT_LONG]
                and connect_string is not None):

            connect_code = validate_connection_string(connect_string)

        # Check if user is wanting to build their connection string
        elif (self.options[HOST_SHORT] or self.options[HOST_LONG]
              and self.options[ID_SHORT] or self.options[ID_LONG]
              and self.options[HOST_NAME] and self.options[DEVICE_ID] is not None):
            # See if the access_key exists
            access_key = self.options[ACCESS_KEY]

            if access_key is not None:
                print("Building connection string with Access Key:")
                connect_string = build_connect_string(self.options[HOST_NAME], self.options[DEVICE_ID],
                                                      self.options[ACCESS_KEY])
                connect_code = validate_connection_string(connect_string)

            elif (self.options[RSA_CERT] is not None
                  and self.options[RSA_KEY] is not None):
                connect_string = build_rsa_connect_string(self.options[HOST_NAME], self.options[DEVICE_ID])
                connect_code = validate_connection_string(connect_string)

        # Must have a connection string before proceeding.  Close session if none is provided.
        else:
            print("Invalid connection criteria")
            exit()

        # Check the connection codes.  If just a string, go ahead and setup connection
        if connect_code == CONNECT_STRING_CODE:
            print("Valid connection string!")
            print("Blast off and start the retrieve message process")
            connect_data = {CONNECT_LONG: connect_string}
            RetrieveMessagesTest(connect_code, connect_data)

        # If it's RSA Token, validate tokens then set up connection
        elif connect_code == CONNECT_STRING_AND_RSA_CODE:
            print("Valid connection string with RSA")
            # See if RSA variables exist
            rsa_cert = validate_rsa_cert(self.options[RSA_CERT])
            rsa_key = validate_rsa_key(self.options[RSA_KEY])

            # Check if user is also passing in connection string and certificates
            if rsa_cert and rsa_key is not None:
                print("\nAttempting connection with connection string and RSA Cert/Keys...")
                connect_data = {CONNECT_LONG: connect_string,
                                CERTIFICATE_LONG: rsa_cert,
                                KEY_LONG: rsa_key}
                RetrieveMessagesTest(connect_code, connect_data)

            else:
                print("Invalid RSA Certificate or Key")
                exit()
