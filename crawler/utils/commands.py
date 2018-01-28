import logging

logger = logging.getLogger("ipx_logger")

COMMAND_HEADER = 0


class Command:
    """
        Class used to handle every command sent and received by crawler's client and host.
    """
    def __init__(self, cmd_id, name, description, in_code, value_required=False):
        """
            Constructor
        :param cmd_id: unique id of the command as positive integer
                       example: 13
        :param name: command's name as string
                     example: Ask client for it's name
        :param in_code: code used to call command as string
                        example: ask_client_name
        :param description: command's description as string
                            example: Get client's name command asks client to send it's name
                                     id: 13
                                     value_required: False
                                     in_code usage: ask_client_name
        :param value_required: specifies if additional info (for instance a value) is required when sending the command.
                               example: set_speed_command(speed_value) would require the speed_value additional info
        """
        if type(cmd_id) is not int or cmd_id < 0:
            error = "Invalid command id: {}!".format(cmd_id) + "\nExpected positive integer type!"
            raise NameError(error)

        if type(name) is not str:
            error = "Invalid command name: {}".format(name) + "\nExpected str type!"
            raise NameError(error)

        if type(in_code) is not str:
            error = "Invalid command in_code: {}".format(in_code) + "\nExpected str type!"
            raise NameError(error)

        if type(description) is not str:
            error = "Invalid command description: {}".format(description) + "\nExpected str type!"
            raise NameError(error)

        if type(value_required) is not bool:
            error = "Invalid command value required attribute: {}".format(value_required) + "\nExpected bool type!"
            raise NameError(error)

        self.id = cmd_id
        self.name = name
        self.in_code = in_code
        self.description = description
        self.value_required = value_required

        logger.debug("Command [" + str(self.in_code) + "] initiated!")

    def get_id(self):
        """
            Get command's id.
        :return: id - integer
        """
        return self.id

    def get_name(self):
        """
            Get command's name.
        :return: name - string
        """
        return self.name

    def get_in_code(self):
        """
            Get command's in_code - in code usage.
        :return: in_code
        """
        return self.in_code

    def get_description(self):
        """
            Get command's description.
        :return: description - string
        """
        return self.description

    def get_value_required(self):
        """
            Get command's value required attribute.
        :return: value_required - bool
        """
        return self.value_required

    def __str__(self):
        """
            Informal” or nicely printable string representation of the object.
        :return: name
        """
        return str(self.name)

    def __unicode__(self):
        """
            Informal” or nicely printable string representation of the object required for older versions of Python.
        :return: name
        """
        return str(self.name)

    def __lt__(self, other_command):
        """
            Method used to be able to sort Command type objects by their name.
        :param other_command: Command object to compare name with
        :return: bool True or False
        """
        return self.name < other_command.name


class Commands:
    """Commands
        Class used to handle commands sent and received by crawler's client and host.
    """
    def __init__(self):
        """Constructor
        """
        self.all_commands = []

        self.drive = Command(
            cmd_id=1,
            name="drive",
            description="Drive Crawler",
            in_code="drive",
            value_required=True,
        )
        self.all_commands.append(self.drive)

        self.steer = Command(
            cmd_id=2,
            name="steer",
            description="Steer Crawler",
            in_code="steer",
            value_required=True,
        )
        self.all_commands.append(self.steer)

        self.__check_for_duplicates__()

    def __check_for_duplicates__(self):
        """
            Check if there are more commands with same id, name or in_code.
        :return: None or raise NameError
        """
        self.__check_for_duplicates_ids__()
        self.__check_for_duplicates_names__()
        self.__check_for_duplicates_in_codes__()

    def __check_for_duplicates_ids__(self):
        """
            Check if there are more commands with same id.
        :return: None or raise NameError
        """
        logger.debug("Checking commands for duplicated IDs...")

        duplicates_found = False
        id_list = []
        for command in self.all_commands:
            id_list.append(command.id)

        id_list = sorted(id_list)
        for id_index in range(0, len(id_list) - 1):
            current_id = id_list[id_index]
            next_id = id_list[id_index + 1]
            if current_id == next_id:
                error = "Found duplicates IDs in commands! ID = {}".format(current_id)
                logger.error(error)
                raise NameError(error)

        if not duplicates_found:
            logger.debug("No commands duplicated by ID.")

    def __check_for_duplicates_names__(self):
        """
            Check if there are more commands with same name.
        :return: None or raise NameError
        """
        logger.debug("Checking commands for duplicated names...")

        duplicates_found = False
        name_list = []
        for command in self.all_commands:
            name_list.append(command.name)

        name_list = sorted(name_list)
        for name_index in range(0, len(name_list) - 1):
            current_name = name_list[name_index]
            next_name = name_list[name_index + 1]
            if current_name == next_name:
                error = "Found duplicates names in commands! ID = {}".format(current_name)
                logger.error(error)
                raise NameError(error)

        if not duplicates_found:
            logger.debug("No commands duplicated by name.")

    def __check_for_duplicates_in_codes__(self):
        """
            Check if there are more commands with same in_code.
        :return: None or raise NameError
        """
        logger.debug("Checking commands for duplicated in_codes...")

        duplicates_found = False
        in_code_list = []
        for command in self.all_commands:
            in_code_list.append(command.in_code)

        in_code_list = sorted(in_code_list)
        for in_code_index in range(0, len(in_code_list) - 1):
            current_in_code = in_code_list[in_code_index]
            next_in_code = in_code_list[in_code_index + 1]
            if current_in_code == next_in_code:
                error = "Found duplicates in_codes in commands! in_code = {}".format(current_in_code)
                logger.error(error)
                raise NameError(error)

        if not duplicates_found:
            logger.debug("No commands duplicated by in_code.")



