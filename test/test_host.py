import logging
import unittest

from crawler.utils.connection.host import Host

logger = logging.getLogger('ipx_logger')


class TestHost(unittest.TestCase):

    def test_001_host_initialization(self):
        logger.info("\n\n1. TestHost")
        logger.info("\n\n\tRunning TestHost - test_host_initialization\n")
        ipx_host = Host()
        self.assertIsInstance(ipx_host, Host)

    def test_002_host_information(self):
        logger.info("\n\n\tRunning TestHost - test_host_information...\n")
        ipx_host = Host()

        host_info = ipx_host.get_info()
        logger.info(host_info)



