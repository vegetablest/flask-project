#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：app_base.py
@Author  ：Su af
@Date    ：2023/2/15 22:03 
"""


class FlaskDefaultConfig():
    SECRET_KEY = "asdfasdf"


class FlaskDevementConfig():
    DEBUG = True
    SECRET_KEY = "dev"


class FlaskProductConfig():
    SECRET_KEY = "prod"


if __name__ == '__main__':
    pass
