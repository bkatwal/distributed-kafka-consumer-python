import os

ROOT_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
USERNAME = os.environ.get('UNIVERSAL_SEARCH_QUS_USERNAME', 'admin')
PASSWORD = os.environ.get('UNIVERSAL_SEARCH_QUS_PASSWORD', 'admin123')
