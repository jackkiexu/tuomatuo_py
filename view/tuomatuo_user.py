# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      tuomatuo_user
   Description :
   Author :         xjk
   date：           8/11/18
-------------------------------------------------
   Change Activity: 8/11/18:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from flask import Flask, request
from core import app, db, log
import requests
from utils.sys_decorator import aspect


@app.route('/jack2', methods=['GET', 'POST'])
def jack2():
    log.info('request.args %s', request.args)
    log.info('request.data %s', request.data)
    log.info('request.headers %s', request.headers)
    log.info('request.form %s', request.form)
    log.info('request.json %s', request.json)

    return 'jack'


@app.route("/hello")
@aspect('')
def hello_world_02():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    log.info( request.headers)
    log.info( request.form)
    log.info( request.form['name'])
    log.info( request.form.get('name'))
    log.info( request.form.getlist('name'))
    log.info( request.form.get('nickname', default='little apple'))
    return 'welcome'

