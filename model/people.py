#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/22 21:54
# @Author   : zhaoqc
# @FileName : people.py
from database import Base, engine
from sqlalchemy import Column, String, Integer


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(12))
    age = Column(Integer)
