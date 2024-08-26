#!/usr/bin/python3 
#coding=utf-8
import asyncio
from aiohttp import web
import json
from langchain_openai import ChatOpenAI

import logging

# __name__表示当前的模块名称
app = web.Application()

logging.basicConfig(level=logging.INFO)
# 配置日志
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
#     # base_url="...",
#     # organization="...",
#     # other params...
# )

async def say_hello(name):
    await asyncio.sleep(1)
    return "Hello, " + name

# 定义url请求路径
async def index(request):
    """定义视图函数"""
    # asyncio.run(say_hello())  
    # 默认值 "Anonymous"
    name = request.match_info.get('name', "Anonymous")
    result = await say_hello(name)
    text = f"<h1>{result}</h1>"
    # content_type="text/html" 识别html
    return web.Response(text=text, content_type="text/html")

def process_data():
	# 请求方式为post时，可以使用 request.get_json()接收到JSON数据
    try:
        data = request.get_json()
        # 如果得到的data是字符串格式，则需要用json.loads来变换成python格式，看个人需求
        # data = json.loads(data)
        # print(data)
        logging.info('请求数据：', data)
        # 获取 POST 请求中的 JSON 数据
    except Exception as e:
        return jsonify({'error': '请求数据失败'}), 400

    # 处理数据
    # 调用do_process_data函数来处理接收到的数据。
    # 判断是否接收到数据
    if data:
        try:
            processed_data = asyncio.run(do_process_data(data))
        except Exception as e:
            return jsonify({'error': '处理数据失败'}), 666

        # 返回的数据格式看请求方的要求了，也有可能需要json处理后的数据，即jsonify(processed_data)
        # return str(processed_data)
        return jsonify(processed_data)

async def do_process_data(reqdata):
    resdata = {
        "code": 'success',
        "data": {
            "model": reqdata.get('model'),
            "chatmsg": '我收到消息，认真解答中...'
        }
    }
    await asyncio.sleep(1)
    logging.info('响应数据：', str(resdata))
    return resdata

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def handle(request):
    name = request.match_info.get("name")
    text = "Hello, " + name
    return web.Response(text=text)

async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


# 添加路由:
app.add_routes([web.get('/', index),
                web.get('/echo', wshandle),
                web.get('/{name}', handle),
                web.post('/process', process_data)])

# def create_app():
#    return app


# __name__ 参数是特殊的Python变量，当脚本被执行时，它的值为'__main__'，这个条件语句保证应用程序只在被作为主程序运行时才会执行
if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)

    # Debug/Development  app.run() 默认5000
    web.run_app(app, host='0.0.0.0', port=9000)
    # app.run(debug=True, host='0.0.0.0', port=5001)

    # Production
    # from gevent.pywsgi import WSGIServer
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()