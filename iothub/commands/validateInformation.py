from iothub.commands.globals import *
from iothub.commands.device_commands import retrieveMessage
from iothub_client import IoTHubTransportProvider
import re
import pem


def build_connect_string(host_name_str, host_name, id_str, id, access_key_str, access_key):
    """
        Build a connection string to retrieve messages from the cloud to the device
        Connection strings without RSA Takes the following format:
        HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
        :param host_name_str: Constant String
        :param host_name: Host Name of IoT Hub
        :param id_str: Either Device ID or Shared Access Name, depending on if user is sending or receiving
        :param id: Device ID of particular device you want to interact with
        :param access_key_str: Constant String for Access Key of above device/shared access name
        :param access_key: Access Key for device referenced above.
        :return: valid connection string
    """
    # print("Building connection string")

    # Todo: 1) check if semi-colons are already at the end of each item passed in
    #       1a) If not, add them
    # Todo: 2) check if ending string "azure-devices.net" is already at the end of host_name
    #       2a) If not, append that to the end
    return '%s%s%s%s%s%s%s%s' % (
        host_name_str, host_name, ';', id_str, id, ';', access_key_str, access_key)


def build_retrieve_rsa_connect_string(host_name, device_id):
    """
        HostName=<host_name>;DeviceId=<device_id>;x509=true
        :param host_name:
        :param device_id:
        :return:
    """
    # print("Building RSA Connection String")
    return "%s%s%s%s%s%s%s" % (HOST_NAME_STR, host_name, ';', DEVICE_ID_STR, device_id, ';', X509_STR)


def validate_connection_string(connect_string):
    """
        Validate connection string received from user
        Connection strings can take the following formats:
        FOR RETRIEVING MESSAGES FROM DEVICE:
        1) HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
            a) Use this connection string if you are connecting straight to device
                without the use of RSA Certs/Keys
        2) HostName=<host_name>;DeviceId=<device_id>;x509=true
            a) Use this Connection string if accompanied with valid keys and
                certificates
        Regex to check if it's a valid connection string (Note, does not actually ping or check.
        It's simply telling whether it's valid based on input.  These values could be anything.
        (HOST_NAME_STR).*(DEVICE_ID_STR).*((x509_STR)|(SHARED_ACCESS_KEY_STR))
        FOR SENDING MESSAGES FROM SERVICE/CLOUD
        1) HostName=<host_name>;SharedAccessName=<access_name>;SharedAccessKey=<device_key>
            a) Use this connection string if you are connecting straight to service to message to device
        :return: True if it is a valid connection string
    """
    # print("Checking provided connection string")
    # print(connect_string)
    if re.match(REGEX_X509_STRING, connect_string):
        # print("Valid x509 connection string...")
        return CONNECT_STRING_AND_RSA_CODE

    elif re.match(REGEX_RETRIEVE_CONNECT_STRING, connect_string):
        # print("Valid access key connection string...")
        return CONNECT_RETRIEVE_STRING_CODE

    elif re.match(REGEX_SEND_CONNECT_STRING, connect_string):
        return CONNECT_SEND_STRING_CODE
    else:
        print("Invalid connection string")
        exit()


def validate_rsa_cert(rsa_cert_file):
    """
    Verify that the RSA Certificate File is in our specific format
    :param rsa_cert_file:
    :return: contents of certificate file
    """
    # print("Validating RSA Certificate: ")
    if check_rsa_file(rsa_cert_file, CERTIFICATE_FILE_HEADER):
        return pem.parse_file(rsa_cert_file)
    else:
        print("Invalid RSA Cert!")
        exit()


def validate_rsa_key(rsa_key_file):
    """
    Verify that the RSA Ke file is in our specific format
    :param rsa_key_file:
    :return: contents of key file
    """
    # print("Validating RSA Key: ")
    if check_rsa_file(rsa_key_file, KEY_FILE_HEADER):
        return pem.parse_file(rsa_key_file)
    else:
        print("Invalid RSA Key!")
        exit()


def check_rsa_file(file, file_header):
    """
    Check the files as they are passed in.
    :param file: File that we are checking
    :param file_header: Header information that we are looking for
    :return: True or False on whether it is the file type we need and in the correct format
    """

    if file_header in open(file).read():
        # print("%s is the correct type of file" % file)
        return True
    else:
        print("%s file not formatted correctly." % file)
        return False


def get_protocol(protocol_string):
    """
    Get the correct protocol from the one provided by the user
    :param protocol_string: Protocol String:
            Can either be AQMP, AQMP WS, MQTT, or HTTP
    :return:
    """
    if protocol_string == "HTTP":
        protocol_type = IoTHubTransportProvider.HTTP

    elif protocol_string == "AMQP":
        protocol_type = IoTHubTransportProvider.AMQP

    elif protocol_string == "MQTT":
        protocol_type = IoTHubTransportProvider.MQTT

    elif protocol_string == "AMQP_WS":
        protocol_type = IoTHubTransportProvider.AMQP_WS

    elif protocol_string == "MQTT_WS":
        protocol_type = IoTHubTransportProvider.MQTT_WS

    else:
        print("Unsupported protocol type. Defaulting to AMQP")
        print("Supported types are: HTTP, AMQP, AMQP_WS, MQTT, MQTT_WS")
        protocol_type = IoTHubTransportProvider.AMQP

    return protocol_type