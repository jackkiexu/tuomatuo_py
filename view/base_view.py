# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      base_view
   Description :
   Author :         xjk
   date：           2018/9/15
-------------------------------------------------
   Change Activity: 2018/9/15:
-------------------------------------------------
"""
from flask import render_template, request
from flask.views import View

__author__ = 'xujiankang'

from core import app


class BaseView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED'
        context = {'users': self.get_users()}
        return self.render_template(context)


class UserView(BaseView):

    def get_template_name(self):
        return 'users.html'

    def get_users(self):
        return [
            {
                'user_name': 'fake',
                'avatar': 'http://localhost:8080'
            }
        ]

