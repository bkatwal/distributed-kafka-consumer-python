from abc import ABC, abstractmethod

from kafka.consumer.fetcher import ConsumerRecord

from src.model.worker_dto import SinkRecordDTO


class StreamTransformer(ABC):

    @abstractmethod
    def transform(self, consumer_record: ConsumerRecord) -> SinkRecordDTO:
        """
        Transforms the JSON for sink updated and extracts the operation associated with the event
        :param consumer_record: kafka consumer record
        :return: return the Sink record that will be put into sink Datastore
        """
