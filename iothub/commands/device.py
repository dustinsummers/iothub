"""The device command"""
from iothub.commands.device_commands import retrieveMessages
from .base import Base


class Device(Base):
    """Check it..."""

    def run(self):
        print('From Device!')
        print('Woohoo!')

        if 'receive' in self.options and self.options["receive"]:
            print("Receive exists and is true!")
            retrieveMessages.retrieve(self)

        else:
            print("seems like somethings messed up!")
