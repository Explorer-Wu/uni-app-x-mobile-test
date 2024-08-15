# aigc-flsak-server
python框架flask构建AIGC应用服务


### pip/conda安装

pip安装参照pip 官网：https://pypi.org/project/pip/

conda安装
`mkdir -p ~/miniconda3`
`curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh`
`bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3`
`rm -rf ~/miniconda3/miniconda.sh`
接着：
`~/miniconda3/bin/conda init bash`
`~/miniconda3/bin/conda init zsh`

你可以通过以下命令来判断是否已安装：
`pip --version`     # Python2.x 版本命令
`pip3 --version`   # Python3.x 版本命令
`conda --version`

### 使用虚拟环境

创建虚拟环境：
`conda create -n <ENV_NAME> python=<VERSION>`
查看服务器存在的虚拟环境:
`conda env list`  或 `conda info -e`
激活指定虚拟环境：
`conda activate <ENV_NAME>`
导出环境(该文件处理环境的 pip 包和 conda 包)：
`conda env export > environment.yml`

### flask框架安装

`pip3 install flask`

给 Flask 安装异步视图支持
`conda install asgiref`

### 启动服务

指定安装包在虚拟环境运行：
`flask --app app run` 或  `FLASK_APP=app.py flask run`

未指定：
`python3 ./app.py`

### asyncio

**协程**
协程，可以看作单线程下多个任务同时进行。
协程的实现方法其实就是迭代器的yield 操作，我们知道在迭代器中，遇到 yield 会中断返回，下次操作时会从这次中断的地方继续执行，在python3.3以后，又加入了yield from 关键字，它后面可以跟迭代器，这样你就可以从一个迭代器中断，进入另一个迭代器去运行，在 asyncio中，await 就相当于 yield from

具体可以看附录第三个问题。

**基础的协程**
以 async def 开始声明一个函数，执行这个函数返回的是一个 cocroutine 对象，函数并不会真的执行（就像执行一个生成器，返回的是一个生成器对象，而不是直接执行代码）
await 会从 cocroutine 获取数据，它调用了这个协程（执行它）
ensure_future/create_task 这两个函数会规划 cocroutine 对象，让它们在下次事件循环（event_loop) 的迭代中去执行（尽管不会去等待它们执行完毕，就像守护进程一样）
创建事件循环，并添加协程对象（Corountine）来执行

**事件循环 event_loop**
事件循环，就相当于一个大池子，这个池子里可以随时添加 Task，它的作用就是调度运行这些 Tasks。它每次只运行一个 Task，一旦当前 Task 遇到 IO 等操作，事件循环会自动调度运行其他的 Task。

有这么几个方法可以创建任务，将任务放到事件循环中：

asyncio.ensure_future(coro_or_future, loop)：这个方法不常用（因为它是python较低版本中使用的方法，更高版本可以使用：asyncio.create_task()）， 它可以指定一个事件循环 loop，不指定的话会默认分配一个 loop。如果第一个参数是 coroutine，则会主动给它创建一个task（通过create_task()方法，这时事件已经存在 loop 中了，并返回 task；如果传参是一个future，则会判断 future 的 loop 和你传递的 loop 是不是同一个 loop，不是的话会报错，是的话直接返回；如果传递的是一个可等待对象，则会将此对象包装一下作为 coroutine ，然后再为它创建一个 task。

asyncio.gather(*args) 会针对每个args，使用 ensure_future() 方法。它返回一个总的 *args的结果列表。

asyncio.create_task(coro) ：（推荐使用）会直接创建一个 task 放到事件循环中，然后事件循环就会自动调度 Task，在某个task中遇到 IO 阻塞时，就会转去执行其他 task 。

### Flask框架的主要特点

1. 轻量级：Flask是一个轻量级的框架，其代码库非常小，并且不需要依赖大量的外部库和工具，因此可以轻松地安装和部署。
2. 灵活性：Flask允许开发者自由选择其他库和工具来扩展其功能，这使得开发者可以根据自己的需求进行灵活的配置。
3. 易于扩展：Flask提供了简单易用的扩展接口，开发者可以使用这些接口来添加新功能或定制框架的行为。
4. Web服务器支持：Flask支持多种Web服务器，如内置的开发服务器、Gunicorn和uWSGI等。
5. RESTful支持：Flask提供了内置的RESTful路由，使得开发RESTful API变得非常容易。
6. Jinja2模板引擎：Flask集成了Jinja2模板引擎，开发者可以使用模板来构建灵活的Web应用程序。
7. Flask-WTF表单：Flask提供了Flask-WTF扩展，使得表单处理变得简单而直观。
8. 内置的调试器：Flask提供了内置的调试器，使得开发者可以轻松地调试和排除错误。
9. 序列化与反序列化：Flask提供了内置的序列化和反序列化功能，使得开发RESTful API变得更加容易。

### python运行报错问题处理

  **mac下安装python3.8以上版本**
  下载安装包后默认标准安装， macOs下终端运行命令：
  `python3 -V` 
  检查python是否安装成功以及python的版本

  **运行.py文件报错permission denied**
  `chmod u+x *.py`
  对当前目录下的*.yp文件的所有者增加可执行权限
  chmod是权限管理命令change the permissions mode of a file的缩写。
  u代表所有者。x代表执行权限。’+’ 表示增加权限。

  **端口号占用问题**

  1. 查看指定端口号
    `lsof  -i:<port>` 或 `lsof -i <tcp>:<port>`

  2. 查看列表中占用端口的PID
  3. 杀死占用端口的进程
    `kill -9 <PID>`

### Flask常用扩展插件
  
  1. Flask-Admin
   Django中有个杀手锏的功能就是自带Admin面板，所有数据都可以通过Admin后台来操作， Flask-Admin 就是一个功能和Django-Admin非常类似的库，有了它你再也不需要直接去数据库查数据改数据了。

  2. Flask-SQLAlchemy
  Flask-SQLAlchemy 扩展了数据库，直接在SQLAlchemy的基础上封装了一层，简化了配置以及SQLAlchemy库的导入路径。

  3. Flask-Migrate 迁移数据库

  4. Flask-JWT-Extended
  前后端分离项目基本都是使用JWT来做用户认证，这是一个用来实现JWT功能的扩展，提供了很多配置参数，非常灵活，直接在config中配置就可以，省去很多造轮子的麻烦。

  5. Flask-Limiter
  Flask-Limiter 用于做接口频率限制的，它可以灵活基于不同资源来限制请求的次数，例如你可以对整个app做限制，页可以对某个blueprint限制，或者是对路由做限制，还支持自定义配置。

  6. Flask-Restful  Restful接口
  7. Flask-Mail 发送邮件
  8. Flask-Cache 缓存处理
  9. Flask-UUID 注册一个uuid的url转换器
  10. Flask-SocketIO  使用Websocket协议进行通讯
  11. Flask-Uploads 文件上传和管理，提供上传、下载和删除操作，支持多种文件格式和上传方式（本地上传、云存储等）
  12. Flask-Moment 本地化日期和时间
  13. Flask-Cors 跨域请求
  14. Flask-BasicAuth 访问认证
  15. Flask-bcrypt 密码加密和校验
  16. flasgger 生成FlaskAPI文档
