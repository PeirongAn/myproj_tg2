#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
This module provide ……
Author: anperiong
Date: 2020/9/15 7:10 下午
@File: my_controller.py
"""
from myproj.model import MyProj
from tgext.crud import EasyCrudRestController


class MyProjController(EasyCrudRestController):
    title = "my_proj"
    model = MyProj
