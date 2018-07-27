import sys
import time
import re
import pem
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError

# HTTP options
# Because it can poll "after 9 seconds" polls will happen effectively
# at ~10 seconds.
# Note that for scalabilty, the default value of minimumPollingTime
# is 25 minutes. For more information, see:
# https://azure.microsoft.com/documentation/articles/iot-hub-devguide/#messaging
TIMEOUT = 241000
MINIMUM_POLLING_TIME = 9

# messageTimeout - the maximum time in milliseconds until a message times out.
# The timeout period starts at IoTHubClient.send_event_async.
# By default, messages do not expire.
MESSAGE_TIMEOUT = 10000

RECEIVE_CONTEXT = 0
WAIT_COUNT = 5
RECEIVED_COUNT = 0
RECEIVE_CALLBACKS = 0

# choose AMQP or AMQP WS as Transport Protocol
PROTOCOL = IoTHubTransportProvider.AMQP

# Connection String Parameters:
# HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
# host_name = Name of the IoT Hub
# Device ID = ID of the device we are trying to connect to
# SharedAccessKey = Key for one of the Shared Accesses
# String containing Hostname, Device Id in the format:
# "HostName=<host_name>;DeviceId=<device_id>;x509=true"
CONNECTION_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true"


# File passed in format: SHA1 Fingerprint=00:00:00:.... (20 Hex passed with it)
def provide_thumbprint(thumbprintFile):
    with open(thumbprintFile, 'r') as myFile:
        sample = myFile.read().replace('\n', '').replace(':', '').split('=')
        print(sample)
    return sample[1]


# Was using this to strip out the thumbprint, but no longer required
# PRIMARY_THUMBPRINT = provide_thumbprint(PRIMARY_THUMBPRINT_FILE)
# SECONDARY_THUMBPRINT = provide_thumbprint(SECONDARY_THUMBPRINT_FILE)

# Print received messages to the console
def receive_message_callback(message, counter):
    global RECEIVE_CALLBACKS
    message_buffer = message.get_bytearray()
    size = len(message_buffer)
    print("Received Message [%d]:" % counter)
    print("     Data: <<<%s>>> & Size=%d" % (message_buffer[:size].decode('utf-8'), size))
    map_properties = message.properties()
    key_value_pair = map_properties.get_internals()
    print("     Properties: %s" % key_value_pair)
    counter += 1
    RECEIVE_CALLBACKS += 1
    print("     Total calls received: %d" % RECEIVE_CALLBACKS)
    return IoTHubMessageDispositionResult.ACCEPTED


# Initialize the client and wait to receive cloud-to-device messages
def iothub_client_init(certificate, key):
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    # client.set_message_callback(receive_message_callback, RECEIVE_CONTEXT)

    # HTTP specific settings
    if client.protocol == IoTHubTransportProvider.HTTP:
        client.set_option("timeout", TIMEOUT)
        client.set_option("MinimumPollingTime", MINIMUM_POLLING_TIME)

    # set the time until a message times out
    client.set_option("messageTimeout", MESSAGE_TIMEOUT)

    # this brings in x509 privateKey and certificate
    client.set_option("x509certificate", str(certificate[0]))
    client.set_option("x509privatekey", str(key[0]))

    #
    if client.protocol == IoTHubTransportProvider.MQTT:
        client.set_option("logtrace", 0)

    client.set_message_callback(
        receive_message_callback, RECEIVE_CONTEXT)
    return client


def iothub_client_sample_run(certificate, key):
    try:
        client = iothub_client_init(certificate, key)

        while True:

            status_counter = 0
            while status_counter <= WAIT_COUNT:
                status = client.get_send_status()
                print("Messages from cloud: %s" % status)
                time.sleep(10)
                status_counter += 1

    except IoTHubError as iothub_error:
        print("Unexpected error %s from IoTHub" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")

    print_last_message_time(client)


def print_last_message_time(client):
    try:
        last_message = client.get_last_message_receive_time()
        print("Last Message: %s" % time.asctime(time.localtime(last_message)))
        print("Actual time: %s" % time.asctime())
    except IoTHubClientError as iothub_client_error:
        if iothub_client_error.args[0].result == IoTHubClientResult.INDEFINITE_TIME:
            print("No message received")
        else:
            print(iothub_client_error)


def usage():
    print("Usage: Simlulatedx509Device.py -p <protocol> -c <cert-file> -k <key-file>")
    print("     protocol    : <amqp, http, mqtt>")
    print("     cert-file   : .PEM File Containing RSA Public Certificate")
    print("     key-file    : .PEM File containing RSA Private Key File")


def check_file_ext(x509_file):
    if not x509_file.endswith('.pem'):
        print("Wrong file extension. Must be a .pem file...\n"
              "python Simulatedx509Device <certificate.pem> <key.pem>")
        exit()

    else:
        return x509_file


def check_file(file, file_header):
    if file_header in open(file).read():
        print("%s is the correct type of file!" % file)
        return file
    else:
        print("File not formatted correctly: %s. \nTry another. ")
        exit()


def retrieve(self):
    print("We are in retrieveMessages")
    # print(self.options)
    if "-C" or "--connection" in self.options and self.options["-C"] is not None:
        if "<connection-string>" in self.options:
            print(self.options["<connection-string>"])



# Main method
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Provide Certificate and Key file before proceeding...\n"
              "python Simulatedx509Device <certificate.pem> <key.pem>")
        exit()

    print("Testing files: %s" % sys.argv)

    # Check that these are .pem files
    x509_certificate_file = check_file_ext(sys.argv[1])
    x509_key_file = check_file_ext(sys.argv[2])

    # Check that the files are what we need
    certificate_test_string = "-----BEGIN CERTIFICATE-----"
    key_test_string = "-----BEGIN RSA PRIVATE KEY-----"
    x509_certificate = pem.parse_file(check_file(x509_certificate_file, certificate_test_string))
    x509_key = pem.parse_file(check_file(x509_key_file, key_test_string))

    print("\n Attempting connection: ")
    print("     Protocol %s" % PROTOCOL)
    print("     Connection string=%s" % CONNECTION_STRING)

    iothub_client_sample_run(x509_certificate, x509_key)
