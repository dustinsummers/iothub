from .Base import Base
from iothub.commands.globals import *
from iothub.commands.service_commands import sendMessage
from .validateInformation import *


class Service(Base):
    """ Sends Messages from the Cloud to the Device """
    print("we made it to send")

    def run(self):
        if 'send' in self.options and self.options["send"]:
            print("we made it to send")
            self.parse_send()

    def parse_send(self):
        """
        Parse values received to craft appropriate message to send to Device
        The following are required for a connection:
        1) Connection String
            a) Host Name
            b) Shared Access Key Name
            c) Shared Access Key (Key for the above name)
        2) Transfer Protocol
            a) AMQP or AMQP_WS (Ports 5671 or 443)
            b) MQTT or MQTT_WS (Ports 8883 or 443)
            c) HTTP (Port 443)
        3) Message to Send
        4) Device to send message to
            SAMPLE CONNECTION_STRING:
            "HostName=<IoTHubName>.azure-devices.net;SharedAccessKeyName=<access-name>;SharedAccessKey=<access=key>"
            :return:
        """
        global connect_data
        connect_string = self.options[CONNECTION_STRING]

        # Check if user is wanting to build their connection string
        if (self.options[HOST_SHORT] or self.options[HOST_LONG]
                and self.options[ACCESS_NAME_LONG] or self.options[ACCESS_NAME_SHORT]
                and self.options[ACCESS_KEY_LONG] or self.options[ACCESS_KEY_SHORT]
                and (self.options[HOST_NAME] and self.options[ACCESS_NAME] and self.options[ACCESS_KEY]) is not None):
            # Create connection string
            connect_string = build_connect_string(HOST_NAME_STR, self.options[HOST_NAME],
                                                  SHARED_ACCESS_NAME_STR, self.options[ACCESS_NAME],
                                                  SHARED_ACCESS_KEY_STR, self.options[ACCESS_KEY])

        # Validate the connection string and retrieve the connection code
        connect_code = validate_connection_string(connect_string)

        # Get the correct protocol
        protocol_type = get_protocol(self.options[PROTOCOL])

        message = self.options[MESSAGE]
        device = self.options[DEVICE_ID]

        # Check the connection code and get the connection data
        if connect_code == CONNECT_SEND_STRING_CODE:
            connect_data = {CONNECT_LONG: connect_string,
                            PROTOCOL: protocol_type,
                            ID_LONG: device,
                            MESSAGE_LONG: message}

        else:
            print("Invalid connection code")
            exit()

        ###
        # Finally launch the message send after gathering up all arguments
        # Program will not reach this point if any of the values were invalid.
        ###
        print("Attempting to connect...")
        service_send = sendMessage(connect_code, connect_data)
        service_send.connect()