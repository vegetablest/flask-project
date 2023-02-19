#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：__init__.py.py
@Author  ：Su af
@Date    ：2023/2/15 21:37 
"""
import json

from flask import Flask, request, g

from application.config.register_base_controller import register_base_controller
from application.config.register_error_handler import register_error_handler
from application.config.register_interceptor import register_interceptor
from ext import db
from application.config.app_config import PhoneConverter
from application.user import user_bp
from flask_migrate import Migrate



def register_bp(app: Flask):
    """
    注册蓝图
    :param app:
    :return:
    """
    # 注册蓝图 代码执行顺序注册了蓝图却没有将蓝图中的url_map加载，所以需要在user模块中的init 最后导入user_view一下，让蓝图的url_map加载好
    app.register_blueprint(user_bp, url_prefix='/user')
    return app


def register_converters(app: Flask):
    """
     注册类型转换器
    :param app:
    """
    app.url_map.converters['phone'] = PhoneConverter

def create_app(config):
    """
    flask application 工厂
    :param config:
    :return:
    """
    # 创建一个Flask application===>SpringBootApplication
    # 传入模块的名字，一般都使用app.py作为工程模块
    app = Flask(__name__)

    # 配置信息
    app.config.from_object(config)
    app.config.from_pyfile('../app_config_file.py')
    # application.config.from_envvar()

    # 初始化db
    db.init_app(app)
    from application.user.user_model import User  # 想要成功这里一定要先导入一下
    # flask db init
    # flask db migrate - m  '第一次模型更新'  ##后面这个-m是注释
    # flask db upgrade                       ##数据库迁移生成表
    migrate = Migrate(app=app, db=db)
    # 拦截器应该在注册视图之前
    register_converters(app)
    register_bp(app)
    register_base_controller(app)
    register_interceptor(app)
    register_error_handler(app)
    return app


if __name__ == '__main__':
    pass
