#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：register_interceptor.py
@Author  ：Su af
@Date    ：2023/2/18 10:32 
"""
from flask import Flask, request, g


def register_interceptor(app: Flask):
    """
    @before_first_request 在对应用程序实例的第一个请求之前注册要运行的函数，只会运行一次。
    @before_request 在每个请求之前注册一个要运行的函数，每一次请求都会执行一次。
    @after_request 在每个请求之后注册一个要运行的函数，每次请求完成后都会执行。需要接收一个 Response 对象作为参数，并返回一个新的 Response 对象，或者返回接收的 Response 对象。
    @teardown_request 注册在每一个请求的末尾，不管是否有异常，每次请求的最后都会执行。
    @context_processor 上下文处理器，返回的字典可以在全部的模板中使用。
    @template_filter('upper') 增加模板过滤器，可以在模板中使用该函数，后面的参数是名称，在模板中用到。
    @errorhandler(400) 发生一些异常时，比如404,500，或者抛出异常(Exception)之类的，就会自动调用该钩子函数。 如果钩子函数没有定义error参数，就会报错。
    @teardown_appcontext 不管是否有异常，注册的函数都会在每次请求之后执行。
    """

    @app.before_first_request
    def before_first_request():
        print("call the before first request of function")

    @app.before_request
    def check_user_status():
        user_name = request.headers.get('user_name')
        if user_name:
            g.user_name = user_name
        else:
            g.user_name = None

    @app.after_request
    def after_request(response):
        print("call the after request of function")
        print(response.headers)
        return response


if __name__ == '__main__':
    pass
