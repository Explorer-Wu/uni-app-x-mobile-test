import asyncio
import logging
from markupsafe import escape
from flask import jsonify, json
import requests
from requests import Request, Session
from ..tools.response import llm_generate_response

from langchain_openai import ChatOpenAI
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
# import getpass
# import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()


async def say_hello(name):
    await asyncio.sleep(1)
    # show the user profile for that user
    return f"Are you {escape(name)}?"


# 使用回调函数
def async_task(callback):
    asyncio.create_task(async_task_impl(callback))


async def async_task_impl(callback):
    await asyncio.sleep(1)
    result = "Hello, Waiting for me"
    callback(result)


# 用在客户端，服务端不可用
async def fetch(
    url,
    method,
    data=None,
    header={},
    stream=True,
    verify=False,
    proxies={},
    cert=None,
    timeout=100,
):
    # session = Session()
    with Session() as session:
        try:
            #     res = requests.get(url)
            method = method.upper()
            req = Request(method, url, data=data, headers=header)
            prepped = req.prepare()

            resp = session.send(
                prepped,
                stream=stream,
                verify=verify,
                proxies=proxies,
                cert=cert,
                timeout=timeout,
            )
            resp.encoding = "utf-8"
            # if resp.status_code == 200:
            return resp.text

        except Exception as e:
            print("Error：", e.args)


async def async_url_join(url):
    await asyncio.sleep(1)
    result = "Hello, " + url
    return result


# openai_apikey = global_conf['llms']['openai_apikey']


async def dodata_llm_openai(reqdata, apikey):
    llmGpt = ChatOpenAI(
        model="gpt-4o-mini",
        # 取样
        temperature=0,
        # 要生成的最大令牌数
        max_tokens=None,
        # 请求超时
        timeout=3000000,
        # 最大重试次数
        max_retries=3,
        # 是否返回logprobs
        # logprobs=false,
        # 配置流式输出
        # stream_options: Dict
        api_key=apikey,  # if you prefer to pass api key in directly instaed of using env vars
        # API 请求的基本 URL。仅在使用代理或服务模拟器时指定
        # base_url="...",
        # OpenAI organization ID,如果未传入，将从环境变量 OPENAI_ORG_ID 中读取
        # organization="...",
        # other params...
    )
    # resdata = {
    #     "code": 'success',
    #     "data": {
    #         "model": reqdata.get('model'),
    #         "chatmsg": '我收到消息，认真解答中...'
    #     }
    # }
    logging.info("响应数据0：", reqdata)
    response = llmGpt.invoke(
        [
            # SystemMessage(content="I am a assistant!"),
            HumanMessage(content=reqdata.get("messages")[0]["content"]),
        ]
    )

    # chunks = []
    # for chunk in response:
    #     chunk_data = json.loads(chunk)
    #     # if "choices" in chunk:
    #     #     text = chunk["choices"][0]["text"]
    #     #     yield text
    #     yield chunks.append(chunk_data)
    # print(chunk.content, end="|", flush=True)
    logging.info("响应数据：", str(parser.invoke(response)))
    return parser.invoke(response)  # llm_generate_response(response)


async def dodata_llm_tongyi(reqdata, apikey):
    logging.info("tongyi数据：", reqdata.get("messages")[0]["content"], apikey)
    llmTongyi = ChatTongyi(
        model=reqdata.get("model"),  # "qwen-turbo",
        # 是否流式传输结果
        streaming=reqdata.get("stream"),
        # 每一步要考虑的标记的总概率质量
        # top_p=0,
        # 生成时重试的最大次数
        # max_retries=2,
        # api_key若未传入，将从环境变量 DASHSCOPE_API_KEY 中读取
        api_key=apikey,
        # base_url="...",
        # organization="...",
        # other params...
    )

    response = llmTongyi.astream(
        [HumanMessage(content=reqdata.get("messages")[0]["content"])],
        streaming=reqdata.get("stream"),
    )
    # chunks = []
    # async for chunk in response:
    #     chunks.append(chunk)
    #     print("chat resp:", type(chunk))
    # logging.info("tongyi响应数据：", str(chunks))
    return response  # str(chunks)
