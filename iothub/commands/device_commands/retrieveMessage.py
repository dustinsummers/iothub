import time
from iothub.commands.globals import *
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessageDispositionResult, IoTHubError

# HTTP options
# Because it can poll "after 9 seconds" polls will happen effectively
# at ~10 seconds.
# Note that for scalability, the default value of minimumPollingTime
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


def receive_message_callback(message, counter):
    global RECEIVE_CALLBACKS
    message_buffer = message.get_bytearray()
    size = len(message_buffer)
    print("\n=-=-=-=-=-\nReceived Message [%d]:" % counter)
    print(" Data: <<<%s>>> & Size=%d" % (message_buffer[:size].decode('utf-8'), size))
    map_properties = message.properties()
    key_value_pair = map_properties.get_internals()
    print("     Properties: %s" % key_value_pair)
    counter += 1
    RECEIVE_CALLBACKS += 1
    print("     Total calls received: %d" % RECEIVE_CALLBACKS)
    print("\n=-=-=-=-=-\n")
    return IoTHubMessageDispositionResult.ACCEPTED


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


def client_connect_string(connection_string, protocol):
    client = IoTHubClient(connection_string, protocol)

    # HTTP Specific Settings
    if client.protocol == IoTHubTransportProvider.HTTP:
        client.set_option(TIMEOUT_STR, TIMEOUT)
        client.set_option(MINIMUM_POLLING_TIME_STR, MINIMUM_POLLING_TIME)

    client.set_option(MESSAGE_TIMEOUT_STR, MESSAGE_TIMEOUT)

    if client.protocol == IoTHubTransportProvider.MQTT:
        client.set_option(LOGTRACE_STR, 0)

    client.set_message_callback(receive_message_callback, RECEIVE_CONTEXT)


def iothub_client_init(connection_string, certificate, key, protocol):
    print("Initializing Connection...")
    client = IoTHubClient(connection_string, protocol)
    client.set_message_callback(receive_message_callback, RECEIVE_CONTEXT)

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

    # print("Setting callback")
    client.set_message_callback(
        receive_message_callback, RECEIVE_CONTEXT)
    return client


def client_connect_rsa(connection_string, certificate, key, protocol):
    try:
        client = iothub_client_init(connection_string, certificate, key, protocol)
        time.sleep(.5)

    except IoTHubError as iothub_error:
        print("Unexpected error %s from IoTHub" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")

    print_last_message_time(client)


class retrieveMessage:
    def __init__(self, connect_code, connect_data):
        self.connect_code = connect_code
        self.connect_data = connect_data

    def connect(self):
        # connection_string = "\"" + self.connect_data[CONNECT_LONG].strip() + "\""
        connection_string = self.connect_data[CONNECT_LONG]
        # print("Connection String: ", connection_string)

        if self.connect_code == CONNECT_STRING_AND_RSA_CODE:
            client_connect_rsa(connection_string,
                               self.connect_data[CERTIFICATE_LONG],
                               self.connect_data[KEY_LONG],
                               self.connect_data[PROTOCOL])

        elif self.connect_code == CONNECT_RETRIEVE_STRING_CODE:
            client_connect_string(connection_string, self.connect_data[PROTOCOL])