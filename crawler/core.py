import logging

from crawler.utils.connection.host import Host
from crawler.utils.commands import Commands
from crawler.utils.motors.mc33926.dual_mc33926_rpi import Motors

logger = logging.getLogger('ipx_logger')


class Crawler:
    """Crawler
        Class used to handle remote controlled device.
    """
    def __init__(self):
        """Constructor
        """
        self.connection = Host()
        self.commands = Commands()
        self.motors = Motors()






