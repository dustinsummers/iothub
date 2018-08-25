from iothub.commands.globals import *
#import getch
import platform

OPEN_CONTEXT = 0
FEEDBACK_CONTEXT = 1
MESSAGE_COUNT = 1


def open_complete_callback(context):
    print('open_complete_callback called with context: {0}'.format(context))


def send_complete_callback(context, messaging_result):
    context = 0
    print('send_complete_callback called with context : {0}'.format(context))
    print('messagingResult : {0}'.format(messaging_result))


def send_device_message(connection_string, device_id, message_str):
    """
    Send a message to your device and handle the feedback message when the device
    acknowledges the cloud-to-device message:
    :param connection_string: Connection string to send message to device
    :param device_id: Name of device to send a message to
    :param message_str: Message to send to device)
    :return:
    """
    # Cannot find any documentation on how to do this...
    from iothub_service_client.iothub_service_client import IoTHubMessaging, IoTHubMessage, IoTHubError

    try:
        iothub_messaging = IoTHubMessaging(connection_string)
        iothub_messaging.open(open_complete_callback, OPEN_CONTEXT)

        for i in range(0, MESSAGE_COUNT):
            print('Sending message: {0}'.format(i))
            msg_txt_formatted = "Sent message: %s" % message_str
            message = IoTHubMessage(bytearray(msg_txt_formatted, 'utf8'))

            # optional: assign ids
            message.message_id = "message_%d" % i
            message.correlation_id = "correlation_%d" % i

            # optional: assign properties
            prop_map = message.properties()
            prop_text = "PropMsg_%d" % i
            prop_map.add("Property", prop_text)

            print (platform.python_version())

            iothub_messaging.send_async(device_id, message, send_complete_callback, i)

            input("Press enter to continue...")

            iothub_messaging.close()

    except IoTHubError as iothub_error:
        print("Unexpected error {0}" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubMessaging sample stopped")


class sendMessage:
    """
        Class to control sending of messages
    """

    def __init__(self, connect_code, connect_data):
        self.connect_code = connect_code
        self.connect_data = connect_data

    def connect(self):
        connection_string = self.connect_data[CONNECT_LONG]

        if self.connect_code == CONNECT_SEND_STRING_CODE:
            send_device_message(connection_string, self.connect_data[ID_LONG],
                                self.connect_data[MESSAGE_LONG])

        else:
            print("Unknown connection code.")
