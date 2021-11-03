from typing import List

from src.model.worker_dto import SinkRecordDTO
from src.stream_writers.stream_writer import StreamWriter
from src.utility import logging_util

logger = logging_util.get_logger(__name__)


class ConsoleStreamWriter(StreamWriter):

    def write(self, streams: List[SinkRecordDTO]) -> None:
        """
        Writes processed records read from kafka to Elastic search
        :param streams: List of SinkRecordDTO - transformed data to be written to ES
        :return: None
        """
        for sink_record_dto in streams:
            print(f' Key: {sink_record_dto.key} - value: {sink_record_dto.message}')

    def close(self) -> None:
        pass
