"""
List of global strings/variables used throughout code
"""

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
MESSAGE_SHORT = "-m"
MESSAGE_LONG = "--message"
MESSAGE = "<message>"
PROTOCOL = "--protocol"
PROTOCOL_HTTP = "HTTP"
PROTOCOL_MQTT = "MQTT"
PROTOCOL_AMQP = "AMQP"

# Values for tracking connection type
CONNECT_RETRIEVE_STRING_CODE = 1001
CONNECT_STRING_AND_RSA_CODE = CONNECT_RETRIEVE_STRING_CODE + 1
CONNECT_SEND_STRING_CODE = CONNECT_STRING_AND_RSA_CODE + 1

# Connection String Constants (for building connection strings)
HOST_NAME_STR = "HostName="
HOST_NAME_END = "azure-devices.net;"
DEVICE_ID_STR = "DeviceId="
SHARED_ACCESS_NAME_STR = "SharedAccessKeyName="
SHARED_ACCESS_KEY_STR = "SharedAccessKey="
X509_STR = "x509=true"

# IoTHub Options
TIMEOUT_STR = "timeout"
MINIMUM_POLLING_TIME_STR = "MinimumPollingTime"
MESSAGE_TIMEOUT_STR = "messageTimeout"
X509_CERTIFICATE_STR = "x509certificate"
X509_PRIVATE_KEY_STR = "x509privatekey"
LOGTRACE_STR = "logtrace"

# REGEX for validating correct connection string
REGEX_X509_STRING = "HostName=.*azure-devices.net;DeviceId=.*;x509=true"
REGEX_RETRIEVE_CONNECT_STRING = "HostName=.*azure-devices.net;DeviceId=.*;SharedAccessKey=.*"
REGEX_SEND_CONNECT_STRING = "HostName=.*azure-devices.net;SharedAccessKeyName=.*;SharedAccessKey=.*"
# Certificate file headers
CERTIFICATE_FILE_HEADER = "-----BEGIN CERTIFICATE-----"
KEY_FILE_HEADER = "-----BEGIN RSA PRIVATE KEY-----"

# Test Connection
TEST_CONNECT_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=Ql3FYv4bUJApyjWNooPbqHgYLGCZlnhsmN/sr3x20FI="
TEST_X509_STRING = "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true"
