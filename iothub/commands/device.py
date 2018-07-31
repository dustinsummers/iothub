"""The device command"""
from iothub.commands.device_commands import RetrieveMessagesTest
from iothub.commands.Strings import *
import re
from .Base import Base
import pem


def get_rsa_cert(self):
    """
    Check if RSA Certificate exists.
    If it does, return certificate.
    If not, return None.
    :return: RSA Certificate
    """

    if (self.options[CERTIFICATE_SHORT]
            or self.options[CERTIFICATE_LONG]
            and self.options[RSA_CERT] is not None):
        print("Retrieving Certificate.")
        return self.options[RSA_CERT]
    else:
        return None


def get_rsa_key(self):
    """
    Check if RSA Key Exists.
    If it does, return key.
    If not, return None.
    :return: RSA Key
    """

    if (self.options[KEY_SHORT]
            or self.options[KEY_LONG]
            and self.options[RSA_KEY] is not None):
        print("Retrieving Key.")
        return self.options[RSA_KEY]
    else:
        return None


def build_connection_string(self):
    """
        Build connection string based on values received
        Connection strings can take the following formats:

        1) HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
            a) Use this connection string if you are connecting straight to device
                without the use of RSA Certs/Keys

        2) HostName=<host_name>;DeviceId=<device_id>;x509=true
            a) Use this Connection string if accompanied with valid keys and
                certificates
        :return: valid connection string
        """
    print("Building connection string")

    return None


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
        return False


def validate_rsa_cert(rsa_cert_file):
    print("Validating RSA Certificate: ")
    if check_file(rsa_cert_file, CERTIFICATE_FILE_HEADER):
        return pem.parse_file(rsa_cert_file)
    else:
        return None


def validate_rsa_key(rsa_key_file):
    print("Validating RSA Key: ")
    if check_file(rsa_key_file, KEY_FILE_HEADER):
        return pem.parse_file(rsa_key_file)
    else:
        return None


def check_file(file, file_header):
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

        # Check if user is attempting to connect with connection string
        if (self.options[CONNECT_SHORT] or self.options[CONNECT_LONG]
                and connect_string is not None):

            connect_code = validate_connection_string(connect_string)

            if connect_code == CONNECT_STRING_CODE:
                print("Valid connection string!")
                print("Blast off and start the retrieve message process")
                connect_data = {CONNECT_LONG: connect_string}
                RetrieveMessagesTest(connect_code, connect_data)

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
        else:
            print("Invalid connection criteria")
            exit()

        #     else:
        #         print("\nAttempting connection with Connecting String only...")
        #         connect_data = {self.options[CONNECT_LONG]: connect_string}
        #         RetrieveMessagesTest(CONNECT_STRING_CODE, connect_data)
        #
        # # Check if user is attempting to connect by providing HostName/DeviceID
        # if (self.options[HOST_SHORT] or self.options[HOST_LONG]
        #         and self.options[ID_SHORT] or self.options[ID_LONG]
        #         and self.options[HOST_NAME] and self.options[DEVICE_ID] is not None):
        #
        #     # User attempting to gain access by building connection string
        #     print("\nHost Name/Device ID Found\nCheck access key or certificate files")
        #
        #     if (self.options[ACCESS_KEY_LONG] or self.options[ACCESS_KEY_SHORT]
        #             and self.options[ACCESS_KEY] is not None):
        #
        #         # User provided Access Key and finished out the connection string
        #         print("\nAccess key found.  Building connection string...")
        #         # Todo: Build function to allow user to build connection string...
        #
        #     elif (self.options[CERTIFICATE_SHORT] or self.options[CERTIFICATE_LONG]
        #           and self.options[KEY_SHORT] or self.options[KEY_LONG]
        #           and self.options[RSA_CERT] and self.options[RSA_KEY] is not None):
        #
        #         # User provided RSA Key and Certificate and wants to connect that way
        #         print("\nRSA-Cert & Key Found!\n Building connection string...")
        #         # Todo: Build function to allow user to build connection string...
