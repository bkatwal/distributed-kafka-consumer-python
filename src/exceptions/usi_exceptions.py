from datetime import datetime


class GenericException(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()


class BadConsumerConfigException(GenericException):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()


class BadInput(GenericException):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()
