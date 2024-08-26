import os
from flask import Blueprint, jsonify, session, request, current_app
from markupsafe import escape

# from .wsApi import wshandle

# from .viewIndex import handle
# from .asyncTest import asynctasks
# from .cbApi import testcb
# from .aichat import fetch_chat_data

from .viewTest import bp as bp_test
from .aichat import aichat_route


# 添加路由:
def setup_routes(app, rootdir):
    # for route in routes:
    # if isinstance(route, Blueprint): db数据库查询方面用到
    app.register_blueprint(bp_test)  # 接口测试

    aichat_route(app)
    # routes = [
    #     bp_test,
    # ]

    # STATIC_DIR = str(rootdir/'static')

    app.add_url_rule("/", endpoint="indexhandle")

    # @app.route('/')
    # def index():
    #     return rh.indexhandle

    # @app.route('/hello/<name>')
    # def hello_user(name):
    #     return rh.indexhandle(name)

    # @app.route('/post/<int:post_id>')
    # def show_post(post_id):
    #     # show the post with the given id, the id is an integer
    #     return f'Post {post_id}'

    # @app.route('/path/<path:subpath>')
    # def show_subpath(subpath):
    #     # show the subpath after /path/
    #     return f'Subpath {escape(subpath)}'
