"""
iothub

Usage:
    iothub hello
    iothub device receive [-C|--connect <connection-string>]
    iothub device receive [-H|--host <host-name>] [-i|--id <device-id>] [-K|--access-key <key>]
    iothub device receive [-C|--connect <connection-string>] [-c|--certificate <cert>] [-k|--key <key>]
    iothub device receive [-H|--host <host-name>] [-i|--id <device-id>] [-c|--certificate <cert-file>] [-k|--key <key-file>]
    iothub service send [-t|--text <text>] [-C|--connect <connection-string>]
    iothub service send [-t|--text <text>] [-H|--host <host-name>] [-N|--access-name <access-name>] [-K|--access-key <access-key>]

Options:
    -C <string>,  --connect <string>           Entire connection string (see example below for sample connection string)
    -H <name>,    --host <name>                Hostname for configuration of ConnectionString
    -N <name>,    --access-name <name>         Shared Access Key Name for configuration of connection String
    -K <key>,     --access-key <key>           Shared Access Key for configuration of Connection String
    -i <id>,      --id <id>                    Device ID for configuration of Connection String
    -h,           --help                       Show this screen.
    -V,           --version                    Show version.
    -c <cert>,    --certificate <cert>         RSA Certificate Provided for access to device
    -k <key>,     --key <key>                  RSA Private Key Provided for access to device
    -t <text,     --text <text>                Text to send in message
Help:
    For help using this tool, please refer to the README.md documentation:
    https://github.com/<provide rest of url>
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import iothub.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined class we've already created.
    for (k, v) in options.items():
        if hasattr(iothub.commands, k) and v:
            module = getattr(iothub.commands, k)
            iothub.commands = getmembers(module, isclass)
            command = [command[1] for command in iothub.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
