#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/22 0:37
# @Author   : zhaoqc
# @FileName : save.py
from bottle import template, Bottle
from bottle import request, FormsDict
from model.people import People
from database import session

save_app = Bottle()


@save_app.route('/')
def save():
    return template('save.html')


@save_app.route('/', method='POST')
def do_save():
    form = request.POST.decode('utf-8')
    p = People()
    p.name = form.get('name')
    p.age = form.get('age')
    session.add(p)
    session.commit()
    return template('save.html')
