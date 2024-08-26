#!/usr/bin/python3
# coding=utf-8
# __init__.py 文件作用：一是包含应用工厂； 二是告诉 Python 当前文件夹应当视作为一个包。

import os
import pathlib
# import asyncio
# import json

import logging

from logging.config import fileConfig
from flask import Flask

from .core.routes import setup_routes
# from tools.utils import load_config

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# pathlib.Path(__file__).parent


def create_app(
    app_config=None,
    root_path=None,
    static_dir="static",
    use_relative_config=True,
    use_instance_config=True,
    use_env_config=True,
    env_config_name="APP_CONFIG_FILE",
):
    """
    创建 flask app
    # import_name,
    # static_url_path: str | None = None,
    # static_host: str | None = None,
    # host_matching: bool = False,
    # subdomain_matching: bool = False
    Args:
        config: 配置信息。

        use_instance_config: 是否加载 instance 配置文件，默认 True 。 当设为 False 时， instance 的相关配置会忽略。
        instance_relative_config: 是否使用 instance 目录，默认 True 。
        instance_path: instance 目录。
        instance_config_file: instance 配置文件名。

        use_env_config: 是否加载 环境变量 配置文件，默认 True 。
        env_config_name: 环境变量名称。

        配置文件加载顺序说明： 首先从 config 中获取配置信息，然后从 instance 中获取配置信息，最后从 环境变量 中获取配置信息。
    """

    # if use_instance_config:
    #     package_path = os.getcwd()
    #     instance_absolute_path = os.path.join(package_path, instance_path)
    # else:
    #     instance_absolute_path = None

    # tmp_dir = pathlib.Path(app_config["TEMPLATE_DIR"])
    # logging.info("Load config:", tmp_dir)
    # instance_path=instance_absolute_path,
    app = Flask(
        __name__,
        static_folder=static_dir,
        # template_folder=app_config["TEMPLATE_DIR"],
        instance_relative_config=use_relative_config,
        root_path=root_path,
    )

    # 加载 log 配置文件
    # fileConfig(app_config["LOG_CONFIG_FILE"])
    # 从 config 中加载配置
    app.config.from_object(app_config)

    # 从环境变量中获取配置文件路径并加载配置
    # if use_env_config:
    #     ret = app.config.from_envvar(env_config_name, silent=True)
    #     app.logger.debug(
    #         "Load config from environment {}.".format("success" if ret else "failed")
    #     )

    # app.config.from_mapping(
    #     # a default secret that should be overridden by instance config
    #     SECRET_KEY="dev",
    #     # store the database in the instance folder
    #     # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    # )

    # 从 instance 文件夹中加载配置
    if app_config is None:
        pass
        # global_conf = load_config(root_path + '/config/config.yml')
        # app.config.from_pyfile(root_path + "/config/config.yml", silent=True)
    else:
        # load the test config if passed in
        app.config.update(app_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # app.logger.info("App create start.")

    setup_routes(app, root_path)

    return app
