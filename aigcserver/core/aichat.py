import asyncio

from flask import current_app, jsonify
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage
# import logging

from .viewApis import RoutesHandler

# from .viewFns import say_hello, do_llm_data
from ..tools.response import ResponseCode, ResponseMessage, RespMsg
# from .viewFns import async_task, async_url_join, fetch

# bp = Blueprint("aichat", __name__, url_prefix="/")


def aichat_route(app):
    rh = RoutesHandler()

    app.add_url_rule(
        "/testcb",
        view_func=rh.testcb,
        methods=["GET"],
    )

    app.add_url_rule(
        "/messages",
        view_func=rh.fetch_chat_data,
        methods=["POST"],
    )

    # def message_api():
    #     return
    # user = get_current_user()
    # return {
    #     "username": user.username,
    #     "theme": user.theme,
    #     "image": url_for("user_image", filename=user.image),
    # }


# @bp.route('/asynctasks')
#     return rh.testlooptask

# import getpass
# import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()
