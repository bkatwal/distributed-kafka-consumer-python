import copy
import json
import os

from src import WORKER_CONFIG_PATH, ROOT_SRC_DIR
from src.exceptions.usi_exceptions import BadInput
from src.utility.common_util import singleton

ENV = os.environ.get('env', 'dev')
AWS_REGION = os.environ.get('aws_region', '')


@singleton
class ConfigManager:

    def __init__(self):
        self._worker_config = None
        self._load_consumer_config()

    def _load_consumer_config(self) -> None:
        with open(ROOT_SRC_DIR + WORKER_CONFIG_PATH, "r") as f:
            self._worker_config = json.load(f)

    def get_worker_config(self) -> list:
        return copy.deepcopy(self._worker_config)

    def get_worker_config_by_name(self, name: str) -> dict:

        for config in self._worker_config:
            if config['consumer_name'] == name:
                return config

        raise BadInput(f'Consumer name: {name}, is not configured.')
