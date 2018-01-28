import logging

from crawler.utils.connection.client import Client
from crawler.utils.commands import Command, Commands, COMMAND_HEADER

logger = logging.getLogger("ipx_logger")


class CrawlerController:
    """CrawlerController
        Class used to handle Crawler's controller.
    """
    def __init__(self, ip, port):
        """Constructor
        """
        self.connection = Client(host=ip, port=port)
        self.commands = Commands()

    def connect_to_crawler(self):
        """connect_to_crawler
            Create connection between Crawler and controller
        :return: None
        """
        self.connection.connect_to_host()

    def __create_package__(self, _header, _id, _value):
        """__create_package__
            Create package to be sent to Crawler
        :return:
        """
        _package = 'h: ' + str(_header) + 'i: ' + str(_id) + 'v: ' + str(_value)
        return _package

    def send_command(self, command, value=None):
        """send_command
            Send a command to Crawler.
        :param command: Command type object.
        :param value: Value to be applied on command (optional).
        :return: None
        """
        if isinstance(command, Command):
            pass
        else:
            logging.warning('Invalid command argument in CrawlerController.send_command(command). Command object '
                            'expected!')
            return

        if command.value_required and value is None:
            logging.warning('Warning! Command {} needs a value specified to be sent! No value provided!'
                            .format(command.name))
            return

        package = self.__create_package__(COMMAND_HEADER, command.id, value)
        self.connection.send_package(package)

    def drive_forward(self, speed):
        """drive_forward
            Tell Crawler to drive forward according to the specified speed.
        :param speed: Speed of the crawler as percentage (PWM duty cycle) - integer ranged [0, 100]
        :return: None
        """
        if speed > 100 or speed < 0:
            logging.warning("Invalid speed value specified in drive_forward! Integer in range [0, 100] expected!")
            return

        speed *= 4.8  # max speed is 480 according to library for the Pololu Dual MC33926 Motor Driver for Raspberry Pi
        speed = int(speed)

        self.send_command(self.commands.drive, speed)

    def drive_backward(self, speed):
        """drive_backward
            Tell Crawler to drive backward according to the specified speed.
        :param speed: Speed of the crawler as percentage (PWM duty cycle) - integer ranged [0, 100]
        :return: None
        """
        if speed > 100 or speed < 0:
            logging.warning("Invalid speed value specified in drive_backward! Integer in range [0, 100] expected!")
            return

        speed *= -4.8  # max speed is 480 according to library for the Pololu Dual MC33926 Motor Driver for Raspberry Pi
        speed = int(speed)

        self.send_command(self.commands.drive, speed)






