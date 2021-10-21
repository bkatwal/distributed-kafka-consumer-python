## Distributed Kafka Consumer Using Ray
Using this project you can create a distributed Kafka Consumers, with the specified number of 
consumers that run on multiple nodes and provides an API support to manage your consumers. 
Operations like - starting/stopping
consumers.

This project uses [Ray](https://docs.ray.io/) to create distributed kafka Consumers

### Setup Instructions

**<ins>Step: 1 - Create Your Transformer Class</ins>**

To create a new transformer implement the abstract class [StreamTransformer](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/transformers/transformer.py) and use 
this new transformer in [worker config](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/config/consumer_config.json).

One example transformer is defined [here](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/transformers/test_transformer.py)

**<ins>Step: 2 - Create your worker config</ins>**

One Example config is defined [here](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/config/consumer_config.json). 
```json
{
    "consumer_name": "some_consumer_group_name",
    "topic_name": "first-topic",
    "number_of_workers": 2,
    "enable_auto_commit": false,
    "bootstrap_servers": "localhost:9092",
    "key_deserializer": "STRING_DES",
    "value_deserializer": "STRING_DES",
    "header_deserializer": null,
    "auto_offset_reset": "earliest",
    "max_poll_records": 20,
    "max_poll_interval_ms": 60000,
    "sink_configs": {
      "transformer_cls": "src.transformers.test_transformer.SampleTransformer"
    },
    "dlq_config": {
      "bootstrap_servers": "localhost:9092",
      "topic_name": "test-dlq",
      "key_serializer": "STRING_SER",
      "value_serializer": "STRING_SER",
      "acks": "all",
      "compression_type": "gzip",
      "retries": 3,
      "linger_ms": 10
    }
  }
```

Config info

Config Name|Description|default value|Is mandatory?|
-----------|-----------|------------|--------------|
consumer_name|This will be used as consumer group name| |Yes
number_of_workers|Number of consumers to create for a consumer group|1|No
sink_configs|Any config related to your sink task. Say, if your are writing to Elasticsearch then you may want to give ES endpoint| |Yes
dlq_config|Dead letter queue config| |No
For available Serializers/deserializers refer [ser_des_util.py](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/kafka_core/ser_des_util.py)

Rest of the configs are self explanatory. 

**<ins>Step: 3 - Install the Requirements</ins>**
Install [requirement.txt](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/requirements.txt)
```shell
pip install -r <path/to/requirement.txt>
```

**<ins>Step: 4 - Run the APP</ins>**
```shell
uvicorn src.event_consumer_app:app --port <port> --reload
```

