import os
import os.path
from typing import Sequence

import yaml


class Config:
    def __init__(self, d: dict,):
        if d is None:
            return

        for k, v in d.items():
            self.__setattr__(k, v)

    def __str__(self):
        return vars(self).__str__()


def load_yaml(path):
    if isinstance(path, str) and os.path.exists(path):
        with open(path) as f:
            return yaml.load(f)
    return {}


def get_config(config_path, defaults=None):
    config = load_yaml(defaults)
    config.update(load_yaml(config_path))

    return config

