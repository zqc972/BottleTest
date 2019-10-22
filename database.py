#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/22 22:58
# @Author   : zhaoqc
# @FileName : database.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()
