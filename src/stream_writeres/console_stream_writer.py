from typing import List

from src.api.stream_writer import StreamWriter
from src.model.worker_dto import SinkRecordDTO


class ConsoleStreamWriter(StreamWriter):

    def write(self, streams: List[SinkRecordDTO]) -> None:
        """
        Writes processed records read from kafka to Elastic search
        :param streams: List of SinkRecordDTO - transformed data to be written to ES
        :return: None
        """
        for sink_record_dto in streams:
            raise Exception('some test')
            print(f'Key: {sink_record_dto.key} - value: {sink_record_dto.message}')

    def close(self) -> None:
        pass