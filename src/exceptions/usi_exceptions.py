from datetime import datetime


class USIException(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()


class BadConsumerConfigException(USIException):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()


class BadInput(USIException):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.when = datetime.now()
