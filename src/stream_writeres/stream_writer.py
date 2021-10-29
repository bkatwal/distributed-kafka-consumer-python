from abc import abstractmethod, ABC


class StreamWriter(ABC):

    @abstractmethod
    def write(self, streams: list) -> None:
        """
        Implement this interface to create an instance of stream writer
        :param streams: key and message dictionary
        :return: None
        """

    @abstractmethod
    def close(self) -> None:
        """
        tear down
        :return:
        """
