import logging
import os
import time


LOG_TO_FILE = False

# create logger
logger = logging.getLogger('ipx_logger')
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s - %(levelname)s: %(message)s", datefmt='%d %b %Y %H:%M:%S')


if LOG_TO_FILE:
    # allow log files creation
    logging.basicConfig(filemode='w')

    logger_file_path = dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + str(r'\logs\log_') + \
                                  str(time.strftime("%d%h%Y_%H%M%S")) + str('.ipx')

    # create file logger handler
    logger_file_handler = logging.FileHandler(logger_file_path)
    logger_file_handler.setLevel(logging.DEBUG)

    logger_file_handler_formatter = logging.Formatter("%(asctime)s: %(message)s",
                                                      datefmt='%d %b %Y %H:%M:%S')
    logger_file_handler.setFormatter(logger_file_handler_formatter)

    logger.addHandler(logger_file_handler)

logger.debug("Initiated logger")
