#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flaskProject 
@File    ：user_view.py
@Author  ：Su af
@Date    ：2023/2/12 18:48 
"""
import json

from flask import request, make_response, session, current_app, g

from application.user import user_bp, requier_loggin
from application.user.user_model import User
from ext import db


@user_bp.route('/zs', methods=["POST", "GET", "PUT"])
def user_list():
    user = {"name": "zs", 'age': 23}
    return user


@user_bp.route('/phone/<int:phone_num>', methods=["GET"])
def user_phone(phone_num=None):
    return str(phone_num)


@user_bp.route('/phone2/<phone_num>', methods=["GET"])
def user_phone2(phone_num=None):
    return phone_num


@user_bp.route('/phone3/<phone:phone_num>', methods=["GET"])
def user_phone3(phone_num=None):
    return phone_num


@user_bp.route('/request', methods=["GET"])
def user_request():
    print(request.path)
    print(request.args.get('aa'))
    print(request.headers)
    print(request.cookies)
    print(request.method)
    return 'phone_num'


@user_bp.route('/request2', methods=["POST"])
def user_request2():
    print(request.path)
    print(request.args.get('aa'))
    print(request.headers)
    print(request.cookies)
    print(request.method)
    print(request.data)
    return 'phone_num'


@user_bp.route('/request3', methods=["POST"])
def user_request3():
    file = request.files['a']
    # try:
    #     with open('./a.png', 'wb') as f:
    #         f.write(file.read())
    # except:
    #     print('error occurs while reading file')
    file.save('./b.png')  # flask 封装的
    return 'upload success'


@user_bp.route('/cookie1', methods=["GET"])
def user_cookie_add():
    resp = make_response('add cookie success')
    resp.set_cookie('name', 'zs')
    return resp


@user_bp.route('/cookie2', methods=["GET"])
def user_cookie_get():
    name = request.cookies.get('name')
    if name:
        return request.cookies.get('name')
    else:
        return '未知'


@user_bp.route('/cookie3', methods=["GET"])
def user_cookie_del():
    resp = make_response('del cookie success')
    resp.delete_cookie('name')
    return resp


@user_bp.route('/session', methods=["GET"])
def user_session_add():
    session['username'] = 'zs'
    return 'success'


@user_bp.route('/session2', methods=["GET"])
def user_session_get():
    name = session['username']
    if name:
        return name
    else:
        return '未知'


@user_bp.route('/session3', methods=["GET"])
def user_session_del():
    session.clear()
    return 'success'


# 请求上下文：request session
# 应用上下文：current_app(application 一般用来写配置信息,或者放redis客户端，数据库客户端，等)
#            g   还有一个是g对象,帮我们保存信息（一次请求有效）,一般钩子函数做认证拦截，然后用户信息放入g函数全局使用

@user_bp.route('/current_app', methods=["GET"])
def user_current_app():
    current_app.config.get('')
    return current_app.config.get('SECRET_KEY')


def get_user_info():
    return '姓名：%s,年龄：%s' % (g.name, g.age)


@user_bp.route('/g', methods=["GET"])
def user_g():
    g.name = 'zs'
    g.age = 23
    return get_user_info()


@user_bp.route('/auth', methods=["GET"])
@requier_loggin  # 加在路由之后
def user_auth():
    return g.user_name


@user_bp.route('/insert/<int:pwd>', methods=["GET"])
def user_insert(pwd: int):
    user = User(username='uname' + str(pwd), password=str(pwd))
    db.session.add(user)
    db.session.commit()
    return user.__str__()


@user_bp.route('/select', methods=["GET"])
def user_select():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    user_list = []
    for user in users:
        user_list.append(user.__str__())
    return json.dumps(users)


if __name__ == '__main__':
    pass
