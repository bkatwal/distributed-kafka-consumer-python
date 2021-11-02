import os
import logging

ROOT_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
USERNAME = os.environ.get('APP_USERNAME', 'admin')
PASSWORD = os.environ.get('APP_PASSWORD', 'admin')

WORKER_NUM_CPUS = os.environ.get('WORKER_NUM_CPUS', .25)

SASL_USERNAME = os.environ.get('SASL_USERNAME', None)
SASL_PASSWORD = os.environ.get('SASL_PASSWORD', None)
SECURITY_PROTOCOL = os.environ.get('SECURITY_PROTOCOL', 'PLAINTEXT')
SASL_MECHANISM = os.environ.get('SASL_MECHANISM')
WORKER_CONFIG_PATH = os.environ.get('WORKER_CONFIG_PATH', '/../config/consumer_config.json')
RAY_HEAD_ADDRESS = os.environ.get('RAY_HEAD_ADDRESS', 'auto')
LOCAL_MODE = os.environ.get('LOCAL_MODE', 'Y')

log_format = '%(asctime)-15s %(name)s: %(message)s'

try:
    open('/var/www-api/.log/consumer_app.log', 'w+')
    logging.basicConfig(filename='/var/www-api/.log/consumer_app.log', format=log_format)
    logging.getLogger().setLevel(logging.INFO)
except BaseException as be:
    logging.error(f'failed to initialize file logging - {be}', )
    logging.basicConfig(format=log_format)
    logging.getLogger().setLevel(logging.INFO)

