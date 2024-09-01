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

### 构建管理工具poetry，初始化&安装依赖包

**安装poetry**
`conda install conda-forge::poetry`

激活指定虚拟环境后，初始化虚拟环境
`poetry env use python`   # 使用当前环境的 Python
`poetry shell`   # 进入虚拟环境
`exit` 停用虚拟环境并退出此新 shell
`conda deactivate` 停用虚拟环境而不离开 shell

**初始化项目包文件pyproject.toml**
`poetry init`
添加主要依赖包：
`poetry add <packName>`

**接手安装项目依赖**
`poetry install` 

该命令的作用：

1. 检查 pyproject.toml 文件中列出的依赖。
2. 如果存在 poetry.lock 文件，Poetry 会根据该文件中锁定的版本来安装依赖。这确保了环境的一致性。
3. 如果不存在 poetry.lock 文件，Poetry 会解析 pyproject.toml 中的依赖并生成一个新的 poetry.lock 文件。
4. 安装所有必要的依赖到项目的虚拟环境中。如果项目的虚拟环境还未创建，Poetry 会先创建它。

**管理环境变量**
Flask的自动发现程序实例机制还有第三条规则：如果安装了python-dotenv，那么在使用flask run或其它命令时会使用它自动从.flaskenv文件和.env文件中加载环境变量。

安装： `poetry add python-dotenv`
当安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量>.env中设置的环境变>.flaskenv设置的环境变量。

  .flaskenv应用于公共变量，用来存储和Flask相关的公开环境变量，比如FLASK_APP；
  而 .env 则用来存储包私有变量(含敏感信息的环境变量)，并且不提交到储存库，比如配置Email服务器的账户名与密码。
  命令行设置的变量会重载 .env 中的变量， .env 中的变量会重载 .flaskenv 中的变量。

**定位错误**
`poetry add dashscope`

**pyproject.toml**
pyproject.toml 是一个标准化的配置文件，定义了Python项目的构建系统和依赖管理。它由 PEP 518 提出，并被广泛接受和使用。这个文件可以包含以下几部分：

1. 构建系统和工具：定义项目使用的构建工具，比如 setuptools 或 poetry。
2. 项目元数据：包括项目的名称、版本、作者、许可证等。
3. 依赖管理：列出项目的依赖项和开发依赖项。

**poetry.toml**
poetry.toml 是一个可选的配置文件，提供了一些额外的配置选项，专门用于配置 Poetry 工具。
  其主要作用如下：

  1. 缓存配置：配置 Poetry 的缓存路径。
  2. 虚拟环境配置：配置虚拟环境的路径、名称等。
  3. 其他本地开发配置：可以配置一些仅限本地开发环境的选项。

### 代码规范检查工具 ruff & pre-commit-hooks

**ruff 安装**
`conda install ruff`

**pre-commit安装**
`conda install pre-commit`

**pre-commit-hooks**
`poetry run pre-commit run --all-files`

### 启动服务

指定安装包在虚拟环境运行：
`flask --app aigcserver run FLASK_ENV=development` 或  `FLASK_APP=aigcserver flask run FLASK_ENV=development`

未指定：
`python3 ./starter.py --dev=development`

`python3 ./starter.py --dev=production`

Local env：
`poetry install`
`FLASK_APP=starter FLASK_ENV=development poetry run flask run`

### 测试

**测试框架安装**
`poetry add pytest --group test`
**运行测试**
`pytest`

**测试覆盖率报告:**
`coverage run -m pytest`
`coverage report`
`coverage html  # open htmlcov/index.html in a browser`

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
