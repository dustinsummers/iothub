"""The device command"""
from iothub.commands.device_commands import RetrieveMessagesTest
from iothub.commands.Strings import *
from .Base import Base


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
        """
        # split out a couple values so we don't have to keep typing self.options
        connect_string = self.options[CONNECTION_STRING]
        rsa_key = self.options[RSA_KEY]
        rsa_cert = self.options[RSA_CERT]

        # Check if user is attempting to connect with connection string
        if (self.options[CONNECT_SHORT] or self.options[CONNECT_LONG]
                and connect_string is not None):

            # Check if user is also passing in connection string and certificates
            if (self.options[CERTIFICATE_SHORT] or self.options[CERTIFICATE_LONG]
                    and self.options[KEY_SHORT] or self.options[KEY_LONG]
                    and rsa_cert and rsa_key is not None):
                print("\nAttempting connection with connection string and RSA Cert/Keys...")
                connect_data = {self.options[CONNECT_LONG]: connect_string,
                                self.options[CERTIFICATE_LONG]: rsa_cert,
                                self.options[KEY_LONG]: rsa_key}
                RetrieveMessagesTest(CONNECT_STRING_AND_RSA, connect_data)

            # Todo: Check to make sure connect string is valid
            else:
                print("\nAttempting connection with Connecting String only...")
                connect_data = {self.options[CONNECT_LONG]: connect_string}
                RetrieveMessagesTest(CONNECT_STRING, connect_data)

        # Check if user is attempting to connect by providing HostName/DeviceID
        if (self.options[HOST_SHORT] or self.options[HOST_LONG]
                and self.options[ID_SHORT] or self.options[ID_LONG]
                and self.options[HOST_NAME] and self.options[DEVICE_ID] is not None):

            # User attempting to gain access by building connection string
            print("\nHost Name/Device ID Found\nCheck access key or certificate files")

            if (self.options[ACCESS_KEY_LONG] or self.options[ACCESS_KEY_SHORT]
                    and self.options[ACCESS_KEY] is not None):

                # User provided Access Key and finished out the connection string
                print("\nAccess key found.  Building connection string...")
                # Todo: Build function to allow user to build connection string...

            elif (self.options[CERTIFICATE_SHORT] or self.options[CERTIFICATE_LONG]
                  and self.options[KEY_SHORT] or self.options[KEY_LONG]
                  and self.options[RSA_CERT] and self.options[RSA_KEY] is not None):

                # User provided RSA Key and Certificate and wants to connect that way
                print("\nRSA-Cert & Key Found!\n Building connection string...")
                # Todo: Build function to allow user to build connection string...

        def build_connection_string():
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

        def validate_connection_string():
            """
            Validate connection string received from user
            Connection strings can take the following formats:

            1) HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>
                a) Use this connection string if you are connecting straight to device
                    without the use of RSA Certs/Keys

            2) HostName=<host_name>;DeviceId=<device_id>;x509=true
                a) Use this Connection string if accompanied with valid keys and
                    certificates

            :return: True if it is a valid connection string
            """
            print("Building Connection String")
