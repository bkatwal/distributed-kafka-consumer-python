import os

ROOT_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
USERNAME = os.environ.get('APP_USERNAME', 'admin')
PASSWORD = os.environ.get('APP_PASSWORD', 'admin123')

WORKER_NUM_CPUS = os.environ.get('WORKER_NUM_CPUS', .25)
