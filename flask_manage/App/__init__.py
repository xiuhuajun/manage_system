from flask import Flask
from App.views import init_view
# from App.models import init_model
from App.ext import init_ext
from App.settings import envs

import logging
from logging.handlers import RotatingFileHandler
# 配置logging在创建app之前，否则将使用默认配置，后续无法更改
# 配置日志记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志处理程序，指明日志路径，每个文件最大大小，保存文件个数上线
file_log_handler = RotatingFileHandler("logs/log",
                                       maxBytes=1024 * 1024 * 100,
                                       backupCount=10)
# 创建日志记录的格式化程序对象    时间 记录器名字 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
)
# 将格式化程序添加到处理程序中
file_log_handler.setFormatter(formatter)
file_log_handler.setLevel(logging.DEBUG)


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))  # 根据开发环境，调用不同的类，配置不同的环境参数

    # 日志
    app.logger.addHandler(file_log_handler)

    # 初始化第三方扩展库
    init_ext(app)
    # 初始化路由
    init_view(app=app)

    return app