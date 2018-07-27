"""
iothub

Usage:
    iothub hello
    iothub device receive -C <string>
    iothub device receive -H <host-name> -d <device-id> -S <key>
    iothub device receive -c <cert-file> -k <key-file> -C <connection-string>
    iothub device receive -c <cert-file> -k <key-file> -H <host-name> -d <device-id>
    iothub service send -t <text> -C <connection-string>
    iothub service send -t <text> -H <host-name> -N <shared-access-key-name> -S <shared-access-key>

Options:
    -C <string>,  --connection <string>        Entire connection string (see example below for sample connection string)
    -H <name>,    --host-name <name>           Hostname for configuration of ConnectionString
    -N <name>,    --access-name <name>         Shared Access Key Name for configuration of connection String
    -S <key>,     --shared-access-key <key>    Shared Access Key for configuration of Connection String
    -d <id>,      --device-id <id>             Device ID for configuration of Connection String
    -h,           --help                       Show this screen.
    -V,           --version                    Show version.
    -c,           --certificate                RSA Certificate Provided for access to device
    -k,           --key                        RSA Private Key Provided for access to device

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
