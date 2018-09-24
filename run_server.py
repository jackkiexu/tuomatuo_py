# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      run_server
   Description :
   Author :         xjk
   date：           8/11/18
-------------------------------------------------
   Change Activity: 8/11/18:
-------------------------------------------------
"""
from view.base_view import UserView

__author__ = 'xujiankang'

from core import app
from view import tuomatuo, tuomatuo_user, filter, earth_map

app.add_url_rule('/users', view_func=UserView.as_view('userview'))

if __name__ == '__main__':
    app.run()




