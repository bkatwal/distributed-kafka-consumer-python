import importlib
from abc import abstractmethod, ABC
from typing import List

from src.exceptions.usi_exceptions import BadInput


class StreamWriter(ABC):

    def __init__(self, config: dict):
        self.config = config

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


def get_stream_writers(cls_paths: List[str], config: dict) -> List[StreamWriter]:
    stream_writers: List[StreamWriter] = []
    for cls_path in cls_paths:
        module_name, class_name = cls_path.rsplit(".", 1)
        stream_writer_cls = getattr(importlib.import_module(module_name), class_name)

        if not issubclass(stream_writer_cls, StreamWriter):
            raise BadInput(f'{cls_path} is not a subclass of StreamTransformer')

        stream_writers.append(stream_writer_cls(config))
    return stream_writers
