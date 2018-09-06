# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      test_concurrent
   Description :
   Author :         xjk
   date：           18/9/1
-------------------------------------------------
   Change Activity: 18/9/1:
-------------------------------------------------
"""
from threading import Thread
from core import log
import time
from utils.concurrent import CountDownLatch
import unittest

__author__ = 'xujiankang'


class TestConncurrent(unittest.TestCase):

    def test_count_down_latch(self):
        class SubThread(Thread):
            def __init__(self, name, latch):
                Thread.__init__(self)
                self.name = name
                self.latch = latch

            def run(self):
                log.info("finishing %s" % self.name)
                time.sleep(3)
                self.latch.count_down();
        latch = CountDownLatch()
        log.info("start main thread")
        thread1 = SubThread("thread first ", latch)
        thread2 = SubThread("thread second ", latch)
        thread3 = SubThread("thread third ", latch)
        thread1.start()
        thread2.start()
        thread3.start()
        latch.await()
        log.info("stop main thread")