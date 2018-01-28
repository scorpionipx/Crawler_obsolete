import logging
import socket as py_socket

logger = logging.getLogger('ipx_logger')


class Host:
    """Host
        Class used to handle internet connection on the crawler as host(slave).
    """
    def __init__(self, host, port=None, username=None, password=None):
        """
            Constructor
        :param host: remote host's name or ip to connect to as string
                     example: '192.168.100.15'
        :param port: host's communication port as integer
                     example: 1369
        :param username: client's username required for authentication as string
                         example: 'RaspberryPIScorpionIPX'
        :param password: client's password required for authentication as string
                         example: 'Qwerty123'
        """
        try:
            logger.debug("Initiating server...")

            # create the socket object
            self.socket = py_socket.socket(py_socket.AF_INET, py_socket.SOCK_STREAM)

            # setting host and port
            self.host = host
            self.port = port

            # setting credentials
            self.username = username
            self.password = password

            self.encoding = 'utf-8'

            logger.debug("Server initiated!")

        except Exception as err:
            error = "Failed to initiate server! " + str(err)
            logger.warning(error)

    def string_to_bytes(self, _string, encoding=None):
        """
            Method converts string type to bytes, using specified encoding.
        Conversion is required for socket's data transfer protocol: string type is not supported.
        :param _string: string to be converted
        :param encoding: character encoding key
        :return: bytes(_string, encoding)
        """
        if encoding is None:
            encoding = self.encoding
        return bytes(_string, encoding)




