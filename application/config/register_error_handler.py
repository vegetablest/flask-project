#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject
@File    ：register_base_controller.py
@Author  ：Su af
@Date    ：2023/2/18 10:33
"""
from flask import Flask


def register_error_handler(app: Flask):
    """
    flask全局异常处理器
    :param app:
    :return:
    """
    from werkzeug.exceptions import HTTPException
    from flask import Response

    @app.errorhandler(code_or_exception=401)
    def error_401(e):
        return Response(r'用户未登录', 401)

    @app.errorhandler(code_or_exception=404)
    def error_404(e):
        return Response(r'not found', 404)

    @app.errorhandler(code_or_exception=405)
    def error_405(e):
        return Response(r'server error', 405)

    @app.errorhandler(HTTPException)
    def error_all(e):
        return Response(r'server error', 500)

    return app


if __name__ == '__main__':
   pass