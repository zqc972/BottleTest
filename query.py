#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/22 1:34
# @Author   : zhaoqc
# @FileName : query.py
from bottle import template, Bottle
from bottle import request
from database import session
from model.people import People

query_app = Bottle()


@query_app.route('/')
def query():
    return template('query.html', results=[])


@query_app.route('/', method='POST')
def do_query():
    form = request.POST.decode('utf-8')
    name = form.get('name')
    # results = session.query(People).filter_by(name=name).all()
    results = session.query(People).filter(People.name.like('%' + name + '%')).all()
    return template('query.html', results=results)
