from flask import request, Response, stream_with_context, current_app
from typing import Any, Optional, Union
import json
from collections.abc import Generator
import logging
from .utils import load_config


class ResponseCode(object):
    Success = 0  # 成功
    Fail = -1  # 失败
    NoResourceFound = 40001  # 未找到资源
    InvalidParameter = 40002  # 参数无效
    AccountOrPassWordErr = 40003  # 账户或密码错误
    VerificationCodeError = 40004  # 验证码错误
    PleaseSignIn = 40005  # 请登陆
    WeChatAuthorizationFailure = 40006  # 微信授权失败
    InvalidOrExpired = 40007  # 验证码过期
    MobileNumberError = 40008  # 手机号错误
    FrequentOperation = 40009  # 操作频繁,请稍后再试


class ResponseMessage(object):
    Success = "成功"
    Fail = "失败"
    NoResourceFound = "未找到资源"
    InvalidParameter = "参数无效"
    AccountOrPassWordErr = "账户或密码错误"
    VerificationCodeError = "验证码错误"
    PleaseSignIn = "请登陆"


class RespMsg(object):
    """
    封装响应文本
    """

    def __init__(self, data=None, code=ResponseCode.Success, req=request):
        # 获取请求中语言选择,默认为中文
        self.lang = req.headers.get("lang", current_app.config.get("LANG", "zh_CN"))
        self._data = data
        self._msg_conf = load_config(
            current_app.config["BASE_DIR"] + current_app.config["RESPONSE_MESSAGE"]
        )
        # logging.info("zh-CN:", self._msg_conf[self.lang])
        self._msg = self._msg_conf[self.lang].get(code, None)
        self._code = code

    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应编码
        :param data: 响应数据
        :param msg: 响应消息
        """
        if code is not None:
            self._code = code
            # 获取对应语言的响应消息
            self._msg = self._msg_conf[self.lang].get(code, None)
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        """
        if name is not None and value is not None:  # and name != "_msg_conf"
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        """
        body = self.__dict__
        body.pop("_msg_conf")
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body


# : Union[dict, RateLimitGenerator]
def llm_generate_response(response) -> Response:
    if isinstance(response, dict):
        return Response(
            response=json.dumps(response), status=200, mimetype="application/json"
        )
    else:

        def generate() -> Generator:
            yield from response
            # for chunk in response:
            #     if isinstance(chunk, str):  # 确保是字符串类型
            #         yield f"data: {chunk}\n\n"  # SSE 格式
            #     else:
            #         # 处理其他可能的返回类型
            #         yield "data: [Non-string output]\n\n"

        return Response(
            stream_with_context(generate()), status=200, mimetype="text/event-stream"
        )
