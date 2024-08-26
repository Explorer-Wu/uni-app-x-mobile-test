#!/usr/bin/python3 
#coding=utf-8
import asyncio
from flask import Flask, request, jsonify

import logging

app = Flask(__name__)
# app = Quart(__name__)

# logging.basicConfig(level=logging.INFO)
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    return "Hello World"

# 定义url请求路径
@app.route('/')
async def index():
    result = await say_hello()
    return f"<h1>{result}</h1>"

async def async_request():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, 'https://www.sina.com.cn')
        return response

async def fetch(session, url):
    async with session.get(url) as response:
        return response.text()

@app.route("/test")
async def test():
    result = await async_request()
    return result

if __name__ == '__main__':
    app.run(debug=True)