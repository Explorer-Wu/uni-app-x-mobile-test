import asyncio
from flask import request, jsonify, json, current_app, Response, stream_with_context
import logging
import os
import datetime
import time
import threading

from .viewFns import (
    async_task,
    async_url_join,
    fetch,
    dodata_llm_openai,
    dodata_llm_tongyi,
)

from ..tools.response import (
    ResponseCode,
    ResponseMessage,
    RespMsg,
    llm_generate_response,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s line:%(lineno)d %(filename)s %(funcName)s >>> %(message)s",
)


class RoutesHandler:
    def __init__(self):
        # self._config = config
        pass

    async def testcb(self):
        # name = request.match_info.get('name', "Anonymous")
        def calltest(result):
            return result

        async_task(calltest)
        # ntext = "Waiting for ..."

        res_json = await fetch("https://www.sina.com.cn/api/hotword.json", "get")
        # print(f"testcb数据： {response}")
        res = RespMsg()
        # test_dict = dict(name="wuwh", age=36)
        res.update(code=ResponseCode.Success, data=res_json)
        return jsonify(res.data)

    async def testlooptask(self):
        async def do_async_tasks():
            urls = [
                "https://www.sina.com.cn/api/hotword.json",
                "https://odin.sohu.com/odin/api/blockdata",
                "https://photo.home.163.com/api/designer/pc/home/index/word",
            ]
            # 准备一个tasks数组
            ntasks = []
            # 对协程对象进行封装为task
            ntasks = [asyncio.create_task(fetch(url, "get")) for url in urls]
            # for url in urls:
            #     # cop = await async_url_join(url)
            #     task = asyncio.create_task(fetch(url))
            #     ntasks.append(task)

            try:
                done, pending = await asyncio.wait(ntasks, timeout=5)
                print("asynctasks数据:", done)
            except asyncio.TimeoutError:
                print("超时啦")
                # 任务被取消：返回 True，没有被取消：返回 False
                for task in pending:
                    task.cancel()
                    print(f"任务 {task} 是否被取消: {task.cancelled()}")

            # return done
            # 得到执行结果
            for do in done:
                res = do.result()
                print(f"{time.time()} 得到执行结果: {res}")

        # 计时
        start = time.time()
        # 把异步方法注册到事件循环中
        # loop = asyncio.get_event_loop()
        loop = asyncio.get_event_loop()
        if loop.is_running():

            def create_loop():
                loop = asyncio.new_event_loop
                asyncio.set_event_loop(loop)
                print("重制事件循环loop:", loop)

                try:
                    loop.run_until_complete(do_async_tasks())
                finally:
                    loop.close()

            threading.Thread(target=create_loop).start()
        else:
            print("正运行的事件循环loop:", loop)

        loop.run_until_complete(do_async_tasks())
        end = time.time()
        total_time = end - start
        logging.info("总耗时:", total_time)

        return str(total_time)

    async def fetch_chat_data(self):
        # 请求方式为post时，可以使用 request.get_json()接收到JSON数据
        try:
            raw_data = request.get_json()
            # 如果得到的data是字符串格式，则需要用json.loads来变换成python格式，看个人需求
            # data = json.loads(data)
            # llm_keys = current_app.config.get("llms")
            # logging.info("请求数据:", llm_keys)
            # 获取 POST 请求中的 JSON 数据
        except Exception as e:
            return jsonify({"error": "请求数据失败"}), 400

        # 处理数据
        # 调用do_process_data函数来处理接收到的数据。
        # 判断是否接收到数据
        if raw_data:
            try:
                # processed_data = asyncio.run(do_process_data(data))

                match raw_data.get("model"):
                    case "gpt-4o-mini" | "gpt-4o" | "gpt-4":
                        # llm_generate_response
                        res_data = await dodata_llm_openai(
                            raw_data,
                            os.getenv("APP_OPENAI_API_KEY"),
                            # llm_keys["openai_apikey"],
                        )
                    case "qwen-turbo" | "qwen-plus":
                        res_data = llm_generate_response(
                            dodata_llm_tongyi(
                                raw_data,
                                os.getenv("APP_ALIBABA_API_KEY"),
                                # llm_keys["alibaba_apikey"],
                            )
                        )
                        # Response(
                        #     stream_with_context(
                        #         dodata_llm_tongyi(
                        #             raw_data,
                        #             llm_keys["alibaba_apikey"],
                        #         )
                        #     ),
                        #     content_type="text/plain",
                        # )
                    case "llama" | "llama3" | "llava":
                        print("score is llama.")
                    case _:  # _表示匹配到其他任何情况
                        print("score is ???.")

                # resp = RespMsg()
                # resp.update(code=ResponseCode.Success, data=res_data)
            except Exception as e:
                print("error " + str(e))
                return jsonify({"error": f"处理数据失败:{raw_data.get("messages")}"})

            # 返回的数据格式看请求方的要求了，也有可能需要json处理后的数据，即jsonify(processed_data)
            return res_data
