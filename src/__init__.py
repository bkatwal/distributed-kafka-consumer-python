import os

ROOT_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
USERNAME = os.environ.get('APP_USERNAME', 'admin')
PASSWORD = os.environ.get('APP_PASSWORD', 'admin123')
