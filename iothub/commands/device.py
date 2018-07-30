"""The device command"""
from iothub.commands.device_commands import RetrieveMessages
from .Base import Base


class Device(Base):
    """Check it..."""

    def run(self):
        if 'receive' in self.options and self.options["receive"]:
            print("Receive exists and is true!")
            RetrieveMessages.retrieve(self)

        else:
            print("seems like somethings messed up!")
