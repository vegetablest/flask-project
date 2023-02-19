#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：register_base_controller.py
@Author  ：Su af
@Date    ：2023/2/18 10:33 
"""
import json

from flask import Flask


def register_base_controller(app: Flask):
    """
       跨域解决原理，拦截所有options请求，然后是符合的域名来的自动给返回相应，且在响应头中加入
       access-control-allow-credentials
       access-control-allow-headers
       access-control-allow-methods
       access-control-allow-origin
    """

    # 注册一个路由  默认GET   OPTIONS, HEAD是HTTP自带的，用来询问接口的信息，不涉及任何业务知识
    @app.route('/')
    def hello_world():
        """
            add 路由
        :return:
        """
        print(app.config['SECRET_KEY'])
        print(app.config['SECRET_VALUE'])
        return 'Hello World!'

    @app.route('/health', methods=["POST", "GET", "PUT"])
    def route_map():
        print(app.url_map)
        return json.dumps({rule.endpoint: rule.rule for rule in app.url_map.iter_rules()})


if __name__ == '__main__':
    pass
