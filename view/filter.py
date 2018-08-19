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
from core import app, log, thread_local
import uuid


@app.before_request
def before_request():
    thread_local.request_id = request.headers.get('HTTP_X_REQUEST_ID', uuid.uuid4().hex)
    log.info('request.headers: %s, request.args: %s, request.data:%s ', request.headers, request.args, request.data)


@app.after_request
def after_request(response):
    thread_local.request_id = ''
    return response