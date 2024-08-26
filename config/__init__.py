#!/usr/bin/python3
# coding=utf-8

import logging
from os import environ, path
from dotenv import load_dotenv
from aigcserver.tools.utils import load_config

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
# BASE_DIR = path.abspath(path.dirname(__file__))
config_path = BASE_DIR + "/config/config.yml"

logging.info("BASE_DIR:", BASE_DIR)

# load_dotenv(path.join(BASE_DIR, ".env"))


def get_config():
    config = load_config(config_path)
    config["BASE_DIR"] = BASE_DIR
    return config
