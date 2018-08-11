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

from flask import Flask
from core import app, db


@app.route('/jack2')
def jack():
    
    return 'jack'