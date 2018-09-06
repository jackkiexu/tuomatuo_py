# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      lo_decorator
   Description :
   Author :         xjk
   date：           2018/9/4
-------------------------------------------------
   Change Activity: 2018/9/4:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from core import log
from date_utils import fmt_d
from functools import wraps


def aspect(msg = None):
    """
    专门打印日志的装饰器
    :param msg:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.info('function %s begin at %s' % (func.__name__, fmt_d(None)))
            try:
                return func(*args, **kwargs)
            finally:
                log.info(' function %s end at %s' % (func.__name__, fmt_d(None)))

        return wrapper
    return decorator