#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：app_config.py
@Author  ：Su af
@Date    ：2023/2/12 17:20 
"""

from werkzeug.routing import BaseConverter


class PhoneConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


if __name__ == '__main__':
    pass
