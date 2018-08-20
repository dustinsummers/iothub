from iothub.commands.validateInformation import *
from iothub.commands.service_commands.sendMessage import *
from .Base import Base


class Service(Base):
    """
        Handles Service Actions: Send (more to come)
        Send: Send a message to a devices message queue
    """

    def run(self):
        if 'send' in self.options and self.options["send"]:
            self.parse_send()

        else:
            print("Unrecognized command")
            exit()

    def parse_send(self):
        """
        Parse values received to craft appropriate message to send to Device
        The following are required to send a message from the service to the device:

        1) Connection String
            a) Host Name (name of the IoTHub Service)
            b) Shared Access Key Name (Name of the Shared Access holder)
            c) Shared Access Key (Key for the above Shared Access name)

            --- SAMPLE CONNECTION_STRING ---
            "HostName=<IoTHubName>.azure-devices.net;SharedAccessKeyName=<access-name>;SharedAccessKey=<access=key>"

        2) Transfer Protocol
            a) AMQP or AMQP_WS (Ports 5671 or 443)
            b) MQTT or MQTT_WS (Ports 8883 or 443)
            c) HTTP (Port 443)

        3) Message to Send to device

        4) Name of device to send message to

            :return:
        """
        global connect_data

        # Set the connect string
        connect_string = self.options[CONNECTION_STRING]

        # Check if user is wanting to build their connection string to check if there are values
        # in the arguments passed via command line
        if (self.options[HOST_SHORT] or self.options[HOST_LONG]
                and self.options[ACCESS_NAME_LONG] or self.options[ACCESS_NAME_SHORT]
                and self.options[ACCESS_KEY_LONG] or self.options[ACCESS_KEY_SHORT]
                and (self.options[HOST_NAME] and self.options[ACCESS_NAME]
                     and self.options[ACCESS_KEY]) is not None):
            # Create connection string based on criteria above
            connect_string = build_connect_string(HOST_NAME_STR, self.options[HOST_NAME],
                                                  SHARED_ACCESS_NAME_STR, self.options[ACCESS_NAME],
                                                  SHARED_ACCESS_KEY_STR, self.options[ACCESS_KEY])

        # Validate the connection string and retrieve the connection code
        connect_code = validate_connection_string(connect_string)

        message = self.options[MESSAGE]
        device = self.options[DEVICE_ID]

        # Get the correct protocol
        # Currently this will throw issues, because importing both iothub_client and
        # iothub_service_client into the same project will throw RunTime warnings about duplicate registrations
        # imports protocol_type = get_protocol(self.options[PROTOCOL])

        # See above error that occurs if we try to include this:

        # if connect_code == CONNECT_SEND_STRING_CODE:
        #     connect_data = {CONNECT_LONG: connect_string,
        #                     PROTOCOL: protocol_type,
        #                     ID_LONG: device,
        #                     MESSAGE_LONG: message}

        # Check the connection code and get the connection data Connect_data is
        # a dictionary of all values passed in via command line and formatted correctly for Azure client Protocol
        if connect_code == CONNECT_SEND_STRING_CODE:
            connect_data = {CONNECT_LONG: connect_string,
                            ID_LONG: device,
                            MESSAGE_LONG: message}

        else:
            print("Invalid connection code")
            exit()

        ###
        # Pass information to the sendMessage command after validating and formatting information
        # Program will not reach this point if any of the values were invalid.
        ###
        print("Attempting to connect...")
        service_send = sendMessage(connect_code, connect_data)
        service_send.connect()
