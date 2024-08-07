#!/usr/bin/python3 
#coding=utf-8
from flask import Flask

# 创建flask的应用对象
# __name__表示当前的模块名称
# 模块名: flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

# 定义url请求路径
@app.route('/')
def index():
    """定义视图函数"""
    return "<h1>Hello, Flask!</h1>"

def create_app():
   return app

# Python 中单行注释以 # 开头
print('Hello World!')

# 多行注释用三个单引号（'''）或者三个双引号（"""）将需要注释的内容囊括起来

a = -50
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m learning\nPython.')

 
'''
函数的测试用例
字符串格式化测试用例
'''
Money = 2000
def AddMoney():
   global Money
   Money = Money + 1
 
print(Money)
AddMoney()
print(Money)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


if __name__ == '__main__':
    # 启动flask  
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)

    # Debug/Development  app.run() 默认5000
    app.run(debug=True, host='0.0.0.0', port=5001)

    # Production
    # from gevent.pywsgi import WSGIServer
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()