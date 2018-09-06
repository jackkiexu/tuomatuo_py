# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      concurrent
   Description :
   Author :         xjk
   date：           18/9/1
-------------------------------------------------
   Change Activity: 18/9/1:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from threading import Condition, Thread
import time


class CountDownLatch(object):

    def __init__(self, count = 1):
        self.count = count
        self.condition = Condition();

    def count_down(self):
        self.condition.acquire()
        self.count -= 1
        if self.count < 0:
            self.condition.notifyAll()
        self.condition.release()

    def await(self):
        self.condition.acquire()
        while self.count > 0:
            self.condition.wait()
        self.condition.release()