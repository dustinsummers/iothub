import random
import sys
import iothub_service_client
import iothub_client
from iothub_client import IoTHubTransportProvider
from iothub_service_client import IoTHubMessaging, IoTHubMessage, IoTHubError


OPEN_CONTEXT = 0
FEEDBACK_CONTEXT = 1
MESSAGE_COUNT = 1

# Connection to the IoTHub controlling the devices
CONNECTION_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey" \
                    "=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o="

PROTOCOL = IoTHubTransportProvider.AMQP

# Device ID for device that we want to send a message to
#DEVICE_ID = "MyPythonDevice"
DEVICE_ID = "thumbprintDevice"

# Print callback messages to the console
def open_complete_callback(context):
    print('open_complete_callback called with context: {0}'.format(context))


def send_complete_callback(context, messaging_result):
    context = 0
    print('send_complete_callback called with context : {0}'.format(context))
    print('messagingResult : {0}'.format(messaging_result))


# Send a message to your device and handle the feedback message when the device
# acknowledges the cloud-to-device message:
def iothub_messaging_sample_run():
    try:
        iothub_messaging = IoTHubMessaging(CONNECTION_STRING)
        iothub_messaging.open(open_complete_callback, OPEN_CONTEXT)

        for i in range(0, MESSAGE_COUNT):
            print('Sending message: {0}'.format(i))
            msg_txt_formatted = "Sent message: %s" % sys.argv[1]
            message = IoTHubMessage(bytearray(msg_txt_formatted, 'utf8'))

            #optional: assign ids
            message.message_id = "message_%d" % i
            message.correlation_id = "correlation_%d" % i

            #optional: assign properties
            prop_map = message.properties()
            prop_text = "PropMsg_%d" % i
            prop_map.add("Property", prop_text)

            iothub_messaging.send_async(DEVICE_ID, message, send_complete_callback, i)

            try:
                # Try Python 2.xx first
                raw_input("Press Enter to continue...\n")
            except:
                pass
                # Use Python 3.xx in the case of exception
                input("Press Enter to continue...\n")

            iothub_messaging.close()

    except IoTHubError as iothub_error:
        print("Unexpected error {0}" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubMessaging sample stopped")


if __name__ == '__main__':
    print("Starting the IoT Hub Service Client Messaging Python sample...")
    print("     Connection string = {0}".format(CONNECTION_STRING))
    print("     Device ID         = {0}".format(DEVICE_ID))

    iothub_messaging_sample_run()