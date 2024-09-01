#!/usr/bin/python3
# coding=utf-8

import logging
import os

from pathlib import Path  # 该方法只能再 3.6以上版本使用
from dotenv import load_dotenv, find_dotenv
from aigcserver.tools.utils import load_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = path.abspath(path.dirname(__file__))
config_path = BASE_DIR + "/config/config.yml"

# logging.info("BASE_DIR:", BASE_DIR)


class LoadEnvFile:
    @staticmethod
    def get_flaskenv():
        load_dotenv(find_dotenv(".flaskenv"), verbose=True, override=True)

    @staticmethod
    def get_env():
        # 自动搜索 .env 文件
        # load_dotenv(verbose=True, encoding="utf-8")

        # 指定.env 文件的位置
        path_env = Path(".env")
        # path_env = os.path.join(BASE_DIR, "/envs/.env")
        load_dotenv(dotenv_path=path_env, verbose=True)


def get_config():
    config = load_config(config_path)
    config["BASE_DIR"] = BASE_DIR
    return config


# if __name__ == "__main__":

LoadEnvFile.get_env()

HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
PORT = os.getenv("FLASK_RUN_PORT")
DEBUG = os.getenv("FLASK_DEBUG", False)

FLASK_ENV = os.getenv("FLASK_ENV")
FLASKENV_TEST = os.getenv("FLASKENV_TEST")
print("FLASKENV:", FLASKENV_TEST)

# print(locals())
