iothub

Usage:
    iothub <command> [options]

Commands
    service
    device

Options:
    -s --send               Send Message (only works with serve ATM)
    -r --retrieve           Retrieve Messages (Only works with device)
    -c --certificate        RSA Certificate Provided for access to device
    -k --key                RSA Private Key Provided for access to device
    -C --connection-string  Entire connection string (see example below for sample connection string)
    -H --host-name          Hostname for configuration of ConnectionString
    -N --shared-access-name Shared Access Key Name for configuration of connection String
    -S -shared-access-key   Shared Access Key for configuration of Connection String
    -d --device-id          Device ID for configuration of Connection String

    -h --help               Show this screen.
    -V --version            Show version.

Examples:
    iothub device -r -c certificate.pem -k key.pem -H <IoTHubName> -d <Device ID>

    iothub service -s -C "HostName=<IoTHubName>.azure-devices.net;SharedAccessKeyName=<SharedAccessName>;SharedAccessKey=<key>"

Help:
    For help using this tool, please refer to the README.md documentation:
    https://github.com/<provide rest of url>