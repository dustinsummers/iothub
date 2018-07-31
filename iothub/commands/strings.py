# Name of CLI
CLI_NAME = "iothub"

# Name of different arguments
DEVICE = "device"
RECEIVE = "receive"
SERVICE = "service"
SEND = "send"
CONNECT_SHORT = "-C"
CONNECT_LONG = "--connect"
CONNECTION_STRING = "<connection-string>"
HOST_SHORT = "-H"
HOST_LONG = "--host"
HOST_NAME = "<host-name>"
ID_SHORT = "-i"
ID_LONG = "--id"
DEVICE_ID = "<device-id>"
ACCESS_KEY_SHORT = "-K"
ACCESS_KEY_LONG = "--access-key"
ACCESS_KEY = "<access-key>"
ACCESS_NAME_SHORT = "-N"
ACCESS_NAME_LONG = "--access-name"
ACCESS_NAME = "<access-name>"
CERTIFICATE_SHORT = "-c"
CERTIFICATE_LONG = "--certificate"
RSA_CERT = "<RSA-cert>"
KEY_SHORT = "-k"
KEY_LONG = "--key"
RSA_KEY = "<RSA-key>"
TEXT_SHORT = "-t"
TEXT_LONG = "--text"
TEXT = "<text>"

# Values for tracking connection type
CONNECT_STRING_AND_RSA_CODE = 1001
CONNECT_STRING_CODE = 1002

# Connection String Constants
HOST_NAME_STR = "HostName="
DEVICE_ID_STR = "azure-devices.net;DeviceId="
SHARED_ACCESS_KEY_STR = "SharedAccessKey="
X509_STR = "x509=true"
REGEX_X509_STRING = "HostName=.*azure-devices.net;DeviceId=.*x509=true"
REGEX_CONNECT_STRING = "HostName=.*azure-devices.net;DeviceId=.*SharedAccessKey="

# Certificate file headers
CERTIFICATE_FILE_HEADER = "-----BEGIN CERTIFICATE-----"
KEY_FILE_HEADER = "-----BEGIN RSA PRIVATE KEY-----"

# Test Connection
TEST_CONNECT_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=g/yFqDtb//4rMTKKkr2UL3Oq0XBCaFRaH1uFam5778k="
TEST_X509_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true"






