#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：app_config.py
@Author  ：Su af
@Date    ：2023/2/12 17:20 
"""

SECRET_VALUE = "value"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

if __name__ == '__main__':
    pass
