from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kafka-connect-dependency',
    version='0.1.1',
    license='MIT',
    url='https://github.com/bkatwal/distributed-kafka-consumer-python',
    author='Bikas Katwal',
    author_email='bikas.katwal10@gmail.com',
    description='Library to run distributed Kafka Consumers using Ray',
    long_description='This library need to be installed in ray nodes. So, ray head and worker '
                     'nodes can find and pickle/unpickle Kafka Consumer modules.',
    keywords=['ray', 'kafka', 'consumer'],
    long_description_content_type="text/markdown",
    py_modules=['src.exceptions.usi_exceptions',
                'src.kafka_core.consumer_manager',
                'src.kafka_core.kafka_stream_writer',
                'src.kafka_core.kafka_util',
                'src.kafka_core.ser_des_util',
                'src.kafka_core.sink_task',
                'src.model.worker_dto',
                'src.stream_writers.stream_writer',
                'src.stream_writers.console_stream_writer',
                'src.transformers.transformer',
                'src.transformers.test_transformer',
                'src.utility.common_util',
                'src.utility.config_manager',
                'src.utility.logging_util'],
    python_requires='>=3',
    install_requires=[
        'fastapi==0.65.1',
        'uvicorn==0.13.4',
        'cachetools~=4.2.2',
        'starlette~=0.14.2',
        'pydantic~=1.7.4',
        'newrelic~=6.8.0.163',
        'ratelimit==2.2.1',
        'ray==1.8.0',
        'kafka-python==2.0.2'
    ]
)
