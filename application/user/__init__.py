#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：__init__.py.py
@Author  ：Su af
@Date    ：2023/2/12 18:54 
"""

from flask import Blueprint, abort, g
user_bp = Blueprint('users', __name__)


# 认证装饰器
def requier_loggin(func):
    def wapper(*args, **keyword):
        if g.user_name is None:
            abort(401)
        else:
            resp = func(*args, **keyword)
            return resp

    return wapper


# init中导入的话 一定要在最后导入视图，在user_bp前边导入的话会出现循环引用
from . import user_view

if __name__ == '__main__':
    pass
