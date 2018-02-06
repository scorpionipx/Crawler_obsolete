import logging

from crawler.utils.connection.host import Host
from crawler.utils.connection.utils.generic import DEFAULT_PORT
from crawler.utils.commands import Command, Commands, COMMAND_HEADER, HEADER_LITERAL, ID_LITERAL, VALUE_LITERAL
from crawler.utils.voice import speak as gtts_speak, LANGUAGE_LITERAL

logger = logging.getLogger('ipx_logger')


class Crawler:
    """Crawler
        Class used to handle remote controlled device.
    """
    def __init__(self, ip=None, port=DEFAULT_PORT):
        """Constructor
        """
        logger.debug("Initializing Crawler...")
        self.connection = Host(forced_ip=ip, port=port)
        self.commands = Commands()
        self.motors = None

        self.__listening__ = False
        logger.debug("Crawler initialized!")

    def connect_with_client(self):
        """connect_with_client
            Connect with a client.
        :return: None
        """
        self.connection.connect_with_client()

    def echo(self):
        """echo
            Crawler echos back every data income from controller.
        :return: None
        """
        self.connection.run_echo_mode()

    def drive(self, speed):
        """drive
            Drive Crawler.
        :param speed: Driving speed. A negative speed means driving backward. Max speed is +- 480, defined in motors'
                        driver specifications.
        :return: None
        """
        logger.debug("Driving [{}]".format(speed))
        # self.motors.motor1.setSpeed(speed)

    def steer(self, steering):
        """steer
            Steer Crawler.
        :param steering: Steering power. A negative steering means steering left . Max steering power is +- 480, defined
                        in motors' driver specifications.
        :return:
        """
        logger.debug("Steering [{}]".format(steering))
        # self.motors.motor2.setSpeed(steering)

    def stop(self):
        """stop
            Stops motor control.
        :return: None
        """
        logger.debug("Motors stopped!")
        # self.motors.setSpeeds(0, 0)

    def disable_motor_control(self):
        """disable_motor_control
            Disables motor control.
        :return: None
        """
        logger.debug("Motor control disabled!")
        # self.motors.disable()

    def enable_motor_control(self):
        """enable_motor_control
            Enables motor control.
        :return: None
        """
        logger.debug("Motor control enabled!")
        # self.motors.enable()

    def speak(self, text):
        """speak
            Speak provided speech.
        :param text: text to be spoken as string.
        :return: None
        """
        speech = text[:text.find(LANGUAGE_LITERAL)]
        language = text[text.find(LANGUAGE_LITERAL) + len(LANGUAGE_LITERAL):]

        logger.debug("Speaking [{}]".format(speech))

        gtts_speak(speech, language)

    def decode_client_command(self, package):
        """decode_client_command
            Decodes packages sent by client. Packages should be intended
        :return: command type object or None and command's value or None
        """
        package = package.decode(self.connection.encoding)
        try:
            header = package[package.find(HEADER_LITERAL) + len(HEADER_LITERAL):package.find(ID_LITERAL)]
            header = int(header)
            cmd_id = package[package.find(ID_LITERAL) + len(ID_LITERAL):package.find(VALUE_LITERAL)]
            cmd_id = int(cmd_id)
            value = package[package.find(VALUE_LITERAL) + len(VALUE_LITERAL):]
            if value.upper() == 'none'.upper():
                value = None
        except Exception as err:
            logger.warning("Unable to decode client's command {}.\n {}".format(package, err))
            return None, None

        if header is not COMMAND_HEADER:
            logger.warning("Tried to decode a command sent with a wrong command header: {}\nHeader {} expected".
                           format(header, COMMAND_HEADER))
            return None, None

        command = self.commands.get_command_by_id(cmd_id)
        return command, value

    def listen(self):
        """listen
            Crawler listens to client's commands.
        :return: None
        """

        if self.connection.client is None:
            self.connect_with_client()

        self.__listening__ = True

        while self.__listening__:
            package_from_client = self.connection.get_package_from_client()
            command, value = self.decode_client_command(package_from_client)
            if isinstance(command, Command):
                self.__execute_command__(command, value)

    def __execute_command__(self, command, value):
        """__execute_command__
            Execute received command.
        :param command: Command object type
        :param value: optional param
        :return: None
        """
        if command is None:
            return

        if command.value_required and value is None:
            logger.warning("No value specified for [{}] command!".format(command))
            return

        if command.id == self.commands.drive.id:
            self.drive(int(value))

        elif command.id == self.commands.steer.id:
            self.steer(int(value))

        elif command.id == self.commands.stop.id:
            self.stop()

        elif command.id == self.commands.enable_motor_control.id:
            self.enable_motor_control()

        elif command.id == self.commands.disable_motor_control.id:
            self.disable_motor_control()

        elif command.id == self.commands.exit.id:
            self.__listening__ = False

        elif command.id == self.commands.speak.id:
            self.speak(value)




