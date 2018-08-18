# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      draw
   Description :
   Author :         xjk
   date：           8/11/18
-------------------------------------------------
   Change Activity: 8/11/18:
-------------------------------------------------
"""
__author__ = 'xujiankang'
from flask import request, Flask
from core import app, log


@app.before_request
def before_request():
    log.info(request.headers)
    log.info(request.args)
    log.info(request.data)