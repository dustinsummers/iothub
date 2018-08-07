"""
Prints out all options passed via command line
Used for debugging purposes
"""


from json import dumps
from .Base import Base


class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print('Hello, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
