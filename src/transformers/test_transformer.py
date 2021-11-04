import json

from kafka.consumer.fetcher import ConsumerRecord

from src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from src.transformers.transformer import StreamTransformer


class SampleTransformer(StreamTransformer):
    def transform(self, consumer_record: ConsumerRecord) -> SinkRecordDTO:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
        :return: SinkRecordDTO
        """
        # do something here
        message_dict: dict = json.loads(consumer_record.value)
        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPSERT
        )

        return SinkRecordDTO(key=consumer_record.key,
                             message=message_dict,
                             topic=consumer_record.topic,
                             offset=consumer_record.offset,
                             sink_operation=sink_operation,
                             partition=consumer_record.partition)
