#!/usr/bin/python3
# coding=utf-8

import yaml
import logging
import os
import click

# from logging.config import dictConfig
from config import get_config, LoadEnvFile, DEBUG, HOST, PORT
from aigcserver import create_app

# from aigcserver.tools.utils import load_config
import pathlib

LoadEnvFile.get_flaskenv()
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s line:%(lineno)d %(filename)s %(funcName)s >>> %(message)s",
# )

BASE_ROOT = pathlib.Path(__file__)

# global global_conf
global_conf = get_config()
# logging.info("global_conf:", str(global_conf))

# 初始化 logging
# log_config_file = global_conf["LOG_CONFIG_FILE"]
# dictConfig(load_config(log_config_file))

# 创建 app
app = create_app(global_conf, BASE_ROOT)


"""
下面这一段代码是根据在命令行中传入的dev的值来执行不同的命令，从而达到一个命令区分开发环境和生产环境
"""


@click.command()
@click.option("--dev", default=os.getenv("FLASK_ENV"), help="environment variable")
def runserver(dev):
    # os.system("FLASK_APP=%s FLASK_ENV=%s FLASK_DEBUG=%s flask run" % (app, dev, DEBUG))
    # flask_env = os.getenv("FLASK_ENV")
    # logging.info("load_dotenv:", dev, DEBUG, HOST, PORT)

    if dev == "production":
        # Production
        # from gevent import monkey
        # monkey.patch_all()
        from gevent.pywsgi import WSGIServer

        http_server = WSGIServer((HOST, int(PORT)), app)
        http_server.serve_forever()

    else:
        app.run(host=HOST, port=int(PORT), debug=DEBUG, load_dotenv=True)


# __name__ 参数是特殊的Python变量，当脚本被执行时，它的值为'__main__'，这个条件语句保证应用程序只在被作为主程序运行时才会执行
if __name__ == "__main__":
    runserver()
