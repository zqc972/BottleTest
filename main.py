 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/21 1:58
# @Author   : zhaoqc
# @FileName : main.py
from bottle import Bottle, template

from database import Base, engine
import form
from save import save_app
from query import query_app

app = Bottle()


@app.route('/')
def index():
    return template('index.html')


if __name__ == '__main__':
    app.mount('/app01', form.form_app)
    app.mount('/save', save_app)
    app.mount('/query', query_app)
    Base.metadata.create_all(engine)
    app.run(host='localhost', port=8000)
