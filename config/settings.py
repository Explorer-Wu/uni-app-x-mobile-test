#!/usr/bin/python3
# coding=utf-8

import logging
import os

from aigcserver.tools.utils import load_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = BASE_DIR + "/config/config.yml"

logging.info("BASE_DIR:", BASE_DIR)


def get_config():
    config = load_config(config_path)
    config["BASE_DIR"] = BASE_DIR
    # if __name__ == '__main__':
    # 	logging.info(config)
    return config
