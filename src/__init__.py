import logging
import os

# set the default logging level to info
logging.basicConfig(level=logging.INFO)

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
