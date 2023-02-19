#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：user_model.py
@Author  ：Su af
@Date    ：2023/2/15 21:32 
"""
from datetime import datetime

from ext import db
import sqlalchemy as sa  # 3.0


# 继承db.model 进而进行orm映射
class User(db.Model):
    't_user'  # 表名
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), unique=True, nullable=False)
    password = sa.Column(sa.String(64), nullable=False)
    phone = sa.Column(sa.String(64), nullable=False, default='123')
    email = sa.Column(sa.String(64), nullable=False, default='7890')
    is_delete = sa.Column(sa.Integer, nullable=False, default=0)
    create_time = sa.Column(sa.DateTime, default=datetime.utcnow())
    update_time = sa.Column(sa.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    # 一对多的正向关系，通过user查询到orders
    # orders = db.relationship('Order', backref='user')

    # db.relationship('order', backref='user') # 通过order中通过userid找到user

    def __str__(self):
        return 'username:%s,password:%s,phone:%s' % (self.username, self.password, self.phone)


if __name__ == '__main__':
    pass
