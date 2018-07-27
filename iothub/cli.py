"""
iothub

Usage:
    iothub hello
    iothub -h | --help
    iothub --version

Options:
    -h --help       Show this screen.
    --version       Show version.

Examples:
    iothub hello

Help:
    For help using this tool, please open an issue on the Github repository:
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
