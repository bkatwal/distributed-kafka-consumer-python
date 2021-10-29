## Distributed Kafka Consumer Using Ray
Using this project you can create a distributed Kafka Consumers, with the specified number of 
consumers that run on multiple nodes and provides an API support to manage your consumers. 
Operations like - starting/stopping
consumers.

This project uses [Ray](https://docs.ray.io/) to create distributed kafka Consumers

### Setup Instructions

**<ins>Step 1 - Create Your Transformer Class</ins>**

To create a new transformer implement the abstract class [StreamTransformer](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/transformers/transformer.py) and use 
this new transformer in [worker config](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/config/consumer_config.json).

One example transformer is defined [here](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/transformers/test_transformer.py)

**<ins>Step 2 - Create your worker config</ins>**

One Example config is defined [here](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/config/consumer_config.json). 
```json
[
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
      "transformer_cls": "src.transformers.test_transformer.SampleTransformer",
      "num_retries": 3,
      "retry_delay_seconds": 1,
      "stream_writers": [
        "src.stream_writers.console_stream_writer.ConsoleStreamWriter"
      ]
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
]

```

Config info

Config Name|Description|default value|Is mandatory?|
-----------|-----------|------------|--------------|
consumer_name|This will be used as consumer group name| |Yes
number_of_workers|Number of consumers to create for a consumer group|1|No
sink_configs|Any config related to your sink task. Say, if your are writing to Elasticsearch then you may want to add ES endpoint in config| |Yes
dlq_config|Dead letter queue config| |No
For available Serializers/deserializers refer [ser_des_util.py](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/src/kafka_core/ser_des_util.py)

Rest of the configs are self explanatory. 

**<ins>Step 3 - Install the Requirements</ins>**

Install all dependencies in [requirement.txt](https://github.com/bkatwal/distributed-kafka-consumer-python/blob/main/requirements.txt)
```shell
pip install -r <path/to/requirement.txt>
```

**<ins>Step 4 - Set necessary Environment Variables</ins>**

Variable Name|Description|Is Mandatory?|Default Value|
-------------|------------|------------|-------------|
APP_USERNAME|Username to setup Basic API Authentication|No|admin|
APP_PASSWORD|Password to setup Basic API Authentication|No|admin|
WORKER_NUM_CPUS|Number of CPUs to reserve per Consumer/Worker|No|0.25|
SECURITY_PROTOCOL|Pass the security protocol being used to connect to Kafka Brokers. Valid values are - PLAINTEXT, SASL_PLAINTEXT, SASL_SSL|No|None|
SASL_MECHANISM|Using using SASL based Auth. Pass either of the valid values - PLAIN, SCRAM-SHA-256, SCRAM-SHA-512|No|None|
SASL_USERNAME|Pass SASL username if using SASL Auth to connect to Kafka|No|None|
SASL_PASSWORD|Pass SASL password if using SASL Auth to connect to Kafka|No|None


**<ins>Step 4 - Run the APP</ins>**
```shell
uvicorn src.event_consumer_app:app --port <port> --reload
```

### License

The MIT License (MIT)

Copyright (c) Bikas Katwal - bikas.katwal10@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




