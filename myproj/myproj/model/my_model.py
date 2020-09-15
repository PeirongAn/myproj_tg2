#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
This module provide ……
Author: anperiong
Date: 2020/9/15 5:55 下午
@File: my_model.py
"""
from myproj.model import DeclarativeBase
from sqlalchemy import Column, Integer, Unicode


class MyProj(DeclarativeBase):
    """

    """
    __tablename__ = 'my_proj'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(16), unique=True, nullable=False)