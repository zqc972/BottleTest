#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/21 3:17
# @Author   : zhaoqc
# @FileName : form.py
from bottle import template, Bottle
from bottle import request

form_app = Bottle()


@form_app.route('/form')
def form():
    return template('form.html')


@form_app.route('/form/login', method='POST')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username, password)
    return 'ok'
