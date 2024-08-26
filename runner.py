#!/usr/bin/python3
# coding=utf-8

import yaml
import logging

# from logging.config import dictConfig
from config import get_config
from aigcserver import create_app

# from aigcserver.tools.utils import load_config
import pathlib

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s line:%(lineno)d %(filename)s %(funcName)s >>> %(message)s",
# )

BASE_ROOT = pathlib.Path(__file__)

# global global_conf
global_conf = get_config()
logging.info("global_conf:", str(global_conf))

# 初始化 logging
# log_config_file = global_conf["LOG_CONFIG_FILE"]
# dictConfig(load_config(log_config_file))

DEBUG, host, port = (
    global_conf["DEBUG"],
    global_conf["server"]["host"],
    global_conf["server"]["port"],
)


# 创建 app
app = create_app(global_conf, BASE_ROOT)

# __name__ 参数是特殊的Python变量，当脚本被执行时，它的值为'__main__'，这个条件语句保证应用程序只在被作为主程序运行时才会执行
if __name__ == "__main__":
    app.run(debug=DEBUG, host=host, port=port)

# Production
# from gevent.pywsgi import WSGIServer
# http_server = WSGIServer(('', 5000), app)
# http_server.serve_forever()
