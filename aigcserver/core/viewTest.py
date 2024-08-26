from flask import Blueprint, render_template, jsonify, request
import logging
from .viewFns import say_hello
from ..tools.response import ResponseCode, ResponseMessage, RespMsg

bp = Blueprint("test", __name__, url_prefix="/")

logger = logging.getLogger(__name__)


# 定义url请求路径
@bp.route("/")
async def indexhandle():
    name = request.args.get("name")
    logging.info("首页：", name)
    result = await say_hello(name)
    return result
    # return render_template("index.html", name="result")


@bp.route("/logs", methods=["GET"])
def test_logger():
    """
    测试自定义logger
    """
    logger.info("this is info")
    logger.debug("this is debug")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")
    return "ok"


@bp.route("/testres", methods=["GET"])
def test_response():
    """
    测试统一返回消息
    """
    res = RespMsg()
    test_dict = dict(name="wuwh", age=36)
    res.update(code=ResponseCode.Success, data=test_dict)
    return jsonify(res.data)
