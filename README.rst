IOTHUB Read Me:

Command Line Interface tool to interface with Microsoft Azure IoTHub.

Look up sample read me formats, and fill this out.

Usage:
    iothub hello
    iothub device receive (-C|--connect) <connection-string>
    iothub device receive (-C|--connect) <connection-string> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key>
    iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-K|--access-key) <access-key>
    iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key>
    iothub service send (-t|--text) <text> (-C|--connect) <connection-string>
    iothub service send (-t|--text) <text> (-H|--host) <host-name> (-N|--access-name) <access-name> (-K|--access-key) <access-key>


Options:
    -C,              --connect                   Entire connection string (see example below for sample connection string)
    -H,              --host                      Hostname for configuration of ConnectionString
    -N,              --access-name               Shared Access Key Name for configuration of connection String
    -K,              --access-key                Shared Access Key for configuration of Connection String
    -i,              --id                        Device ID for configuration of Connection String
    -h,              --help                      Show this screen.
    -V,              --version                   Show version.
    -c,              --certificate               RSA Certificate Provided for access to device
    -k,              --key                       RSA Private Key Provided for access to device
    -t,              --text                      Text to send in message
    --protocol=<protocol>                        Protocol to use. [default: AMQP]
Help:
    For help using this tool, please refer to the README.md documentation:
    https://github.com/<provide rest of url>
