import importlib
from abc import ABC, abstractmethod

from kafka.consumer.fetcher import ConsumerRecord

from src.exceptions.usi_exceptions import BadInput
from src.model.worker_dto import SinkRecordDTO


class StreamTransformer(ABC):

    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def transform(self, consumer_record: ConsumerRecord) -> SinkRecordDTO:
        """
        Transforms the JSON for sink updated and extracts the operation associated with the event
        :param consumer_record: kafka consumer record
        :return: return the Sink record that will be put into sink Datastore
        """


def get_transformer(cls_path: str, config: dict) -> StreamTransformer:
    module_name, class_name = cls_path.rsplit(".", 1)
    stream_transformer = getattr(importlib.import_module(module_name), class_name)

    if not issubclass(stream_transformer, StreamTransformer):
        raise BadInput(f'{cls_path} is not a subclass of StreamTransformer')

    return stream_transformer(config)
