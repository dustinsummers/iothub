from iothub.commands.Strings import *
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
RECEIVED_CALLBACKS = 0


class RetrieveMessagesTest:
    def __init__(self, connect_code, connect_data):
        self.connect_code = connect_code
        self.connect_data = connect_data

    def connect(self):
        connection_string = self.connect_data[CONNECT_LONG]

        if self.connect_code == CONNECT_STRING_AND_RSA_CODE:
            self.client_connect_rsa(connection_string,
                                    self.connect_data[CERTIFICATE_LONG],
                                    self.connect_data[KEY_LONG],
                                    self.connect_data[PROTOCOL])

        elif self.connect_code == CONNECT_STRING_CODE:
            self.client_connect_string(connection_string, self.connect_data[PROTOCOL])

    def client_connect_rsa(self, connection_string, certificate, key, protocol):
        print("Connection String: ", connection_string)
        print("Protocol: ", protocol)
        print(type(connection_string))
        client = IoTHubClient(connection_string, protocol)

        # HTTP Specific Settings
        if client.protocol == IoTHubTransportProvider.HTTP:
            client.set_option(TIMEOUT_STR, TIMEOUT)
            client.set_option(MINIMUM_POLLING_TIME_STR, MINIMUM_POLLING_TIME)

        # set the time until a message times out
        client.set_option(MESSAGE_TIMEOUT_STR, MESSAGE_TIMEOUT)

        # this brings in x509 private key and certificate
        client.set_option(X509_CERTIFICATE_STR, certificate)
        client.set_options(X509_PRIVATE_KEY_STR, key)

        if client.protocol == IoTHubTransportProvider.MQTT:
            client.set_option(LOGTRACE_STR, 0)

        client.set_message_callback(self.receive_message_callback, RECEIVE_CONTEXT)

    def client_connect_string(self, connection_string, protocol):
        # client = IoTHubClient(connection_string, protocol)
        print("Don't do anything yet...")

    def receive_message_callback(self, message, counter):
        global RECEIVE_CALLBACKS
        message_buffer = message.get_bytearray()
        size = len(message_buffer)
        print("Received Message [%d]:" % counter)
        print(" Data: <<<%s>>> & Size=%d" % (message_buffer[:size].decode('utf-8'), size))
        map_properties = message.properties()
        key_value_pair = map_properties.get_internals()
        print("     Properties: %s" % key_value_pair)
        counter += 1
        RECEIVE_CALLBACKS += 1
        print("     Total calls received: %d" % RECEIVE_CALLBACKS)
        return IoTHubMessageDispositionResult.ACCEPTED
