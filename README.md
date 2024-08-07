# aigc-flsak-server
python框架flask构建AIGC应用服务


### pip安装和flask框架安装

pip安装参照pip 官网：https://pypi.org/project/pip/

你可以通过以下命令来判断是否已安装：
`pip --version`     # Python2.x 版本命令
`pip3 --version`   # Python3.x 版本命令

`pip3 install flask`

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

