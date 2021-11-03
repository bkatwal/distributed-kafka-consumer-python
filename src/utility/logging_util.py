import logging
import os

LOG_FILE_PATH = '/var/www-api/.log/consumer_app.log'
LOG_DIR_PATH = '/var/www-api/.log'
LOG_FORMATTER = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'


def is_valid_path(path: str):
    if os.path.exists(path) or os.access(os.path.dirname(path), os.W_OK):
        return True
    return False


def get_logger(name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    std_out_handler = StdOutHandler()
    std_out_handler.setLevel(logging.INFO)
    logger.addHandler(std_out_handler)

    if is_valid_path(LOG_DIR_PATH):
        file_out_handler = FileOutHandler()
        file_out_handler.setLevel(logging.INFO)
        logger.addHandler(file_out_handler)

    return logger


class StdOutHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(StdOutHandler, self).__init__()

    def format(self, record):
        self.formatter = logging.Formatter(LOG_FORMATTER)
        return super(StdOutHandler, self).format(record)


class FileOutHandler(logging.FileHandler):
    def __init__(self):
        super(FileOutHandler, self).__init__(filename=LOG_FILE_PATH)

    def format(self, record):
        self.formatter = logging.Formatter(LOG_FORMATTER)
        return super(FileOutHandler, self).format(record)
