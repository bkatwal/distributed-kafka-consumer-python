from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kafka-sink-connect-python',
    version='0.0.1',
    url='https://github.com/bkatwal/distributed-kafka-consumer-python',
    author='Bikas Katwal',
    author_email='bikas.katwal10@gmail.com',
    description='Notifies in Slack channel with a list of jira tickets that have pending review from x days. Adds the reviewer and PR details if exists.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['src'],
    license='MIT',
    python_requires='>=3',
    install_requires=[
        'fastapi==0.65.1',
        'uvicorn==0.13.4',
        'cachetools~=4.2.2',
        'starlette~=0.14.2',
        'pydantic~=1.7.4',
        'newrelic~=6.8.0.163',
        'ratelimit==2.2.1',
        'ray==1.7.0',
    ]
)
