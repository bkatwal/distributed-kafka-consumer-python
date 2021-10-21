from kafka import KafkaConsumer

TWO_MINUTES = 2


def is_end_offset_none(end_offsets: dict, start_offsets: dict) -> bool:
    """
    Utility function to check if the partition that has start offset has end offset too.
    :param end_offsets: topic partition and end offsets
    :param start_offsets:topic partition and start offsets
    :return: True/False
    """
    if len(end_offsets) == 0:
        return True

    for tp, offset in end_offsets.items():
        if offset is None and start_offsets[tp] is not None:
            return True

    return False


def is_all_end_offset_found(end_offsets: dict, start_offsets: dict) -> bool:
    """
    Utility function to check if the partition that has start offset has end offset too.
    :param end_offsets: topic partition and end offsets
    :param start_offsets:topic partition and start offsets
    :return: True/False
    """
    if len(end_offsets) == 0:
        return False

    for tp, offset in end_offsets.items():
        if offset is None and start_offsets[tp] is not None:
            return False

    return True


def get_start_end_offsets(start_timestamp: int, end_timestamp: int,
                          topic_partitions: set, consumer: KafkaConsumer):
    """
    Get start and end offset for all the partitions based on the given start and end timestamp
    :param start_timestamp: start timestamp in epoch time millis
    :param end_timestamp: end timestamp in epoch time millis
    :param topic_partitions: topic partition set
    :param consumer: kafka consumer
    :return: tuple of start offsets and end offsets for each partition
    """
    tp_start_timestamps: dict = {}
    for tp in topic_partitions:
        tp_start_timestamps[tp] = start_timestamp

    start_offsets = consumer.offsets_for_times(tp_start_timestamps)
    end_offsets = {}
    # go back 2 minute and keep checking if there are end offsets in partition
    tp_end_timestamps: dict = {}
    while not is_all_end_offset_found(start_offsets=start_offsets, end_offsets=end_offsets):
        for tp in topic_partitions:
            # seek previous offset from a partition only if the offset is not found
            if len(end_offsets) == 0 or (end_offsets[tp] is None and start_offsets[tp] is not
                                         None):
                tp_end_timestamps[tp] = end_timestamp

        end_offsets = consumer.offsets_for_times(tp_end_timestamps)
        end_timestamp = end_timestamp - (TWO_MINUTES * 60 * 1000)

    return start_offsets, end_offsets
