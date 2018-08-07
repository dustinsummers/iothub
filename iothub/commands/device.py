"""The device command"""
from iothub.commands.device_commands import retrieveMessage
from .validateInformation import *
from .Base import Base


class Device(Base):
    """
        Handles Device Actions: Receive (more to come)

        Receive: Check Device Message Queue to see if there any new messages, and display those to user.
                 At this time, this is a one time check, and will need to be run each time to see if new messages have arrived.
                 In future, will write new action to "listen" for when new messages arrive
    """

    def run(self):
        if 'receive' in self.options and self.options["receive"]:
            # If receive, parse the self options to determine exact parameters
            self.parse_receive()

        else:
            print("Unrecognized command")
            exit()

    def parse_receive(self):
        """
        Parse values received to craft appropriate retrieval message for IoT Hub
        The following values are required for a connection:
        1) Connection String
            a) Host Name
            b) Device ID
            c) SharedAccess Key Or x509=true(certificate based connection)
       2) Transfer Protocol
            a) AMQP or AMQP_WS (Ports 5671 or 443)
            b) MQTT or MQTT_WS (Ports 8883 or 443)
            c) HTTP (Port 443)
        3) RSA Connection Certs (if connecting using certificates)
            a) RSA Certificate
            b) RSA Key
        """

        # Check Connection String
        global connect_data
        global connect_code
        connect_string = self.options[CONNECTION_STRING]

        # Check if user is wanting to build their connection string
        if (self.options[HOST_SHORT] or self.options[HOST_LONG]
                and self.options[ID_SHORT] or self.options[ID_LONG]
                and (self.options[HOST_NAME] and self.options[DEVICE_ID]) is not None):
            # See if the access_key exists
            access_key = self.options[ACCESS_KEY]

            # Build connection string with access key
            if access_key is not None:
                print("Building connection string with Access Key:")
                connect_string = build_connect_string(HOST_NAME_STR,self.options[HOST_NAME],
                                                      DEVICE_ID_STR, self.options[DEVICE_ID],
                                                      SHARED_ACCESS_KEY_STR, self.options[ACCESS_KEY])

            # Build connection string with x509 = true
            elif (self.options[RSA_CERT] is not None
                  and self.options[RSA_KEY] is not None):
                connect_string = build_retrieve_rsa_connect_string(self.options[HOST_NAME], self.options[DEVICE_ID])

        # Validate the connection string and retrieve connect code
        connect_code = validate_connection_string(connect_string)

        # Get the correct protocol
        protocol_type = get_protocol(self.options[PROTOCOL])

        # Check the connection codes and get the connection data
        if connect_code == CONNECT_RETRIEVE_STRING_CODE:
            connect_data = {CONNECT_LONG: connect_string,
                            PROTOCOL: protocol_type}

        # If it's RSA Token, validate before moving forward
        elif connect_code == CONNECT_STRING_AND_RSA_CODE:
            # See if RSA variables exist
            rsa_cert = validate_rsa_cert(self.options[RSA_CERT])
            rsa_key = validate_rsa_key(self.options[RSA_KEY])
            connect_data = {CONNECT_LONG: connect_string,
                            CERTIFICATE_LONG: rsa_cert,
                            KEY_LONG: rsa_key,
                            PROTOCOL: protocol_type}

        else:
            print("Invalid connection code")
            exit()

        ###
        # Finally launch the message retrieval after gathering up all arguments
        # Program will not reach this point if any of the values were invalid.
        ###
        print("Attempting to connect...")
        device_retrieve = retrieveMessage(connect_code, connect_data)
        device_retrieve.connect()
