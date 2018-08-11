# -*- encoding: utf8 -*-
import time


def stamp_ms(c_time):
    """
    :param c_time: 时间戳(秒单位)
    :return: u'时间戳(毫秒单位)'
    """
    if c_time is None:
        c_time = time.time()

    curr_t = int(c_time * 1000)

    return curr_t


def fmt_d(c_time, fmt_str=None):
    if c_time is None:
        c_time = time.time()
    if fmt_str is None:
        fmt_str = "%Y-%m-%d %H:%M:%S"
    return time.strftime(fmt_str, time.localtime(c_time))

def stamp_time(time_str, fmt_str=None):
    """
    :param time_str:
    :param fmt_str:
    :return:
    """
    if time_str is None or len(time_str) == 0:
        return None
    if fmt_str is None:
        fmt_str = "%Y-%m-%d %H:%M:%S"
    try:
        time_array = time.strptime(time_str, fmt_str)
        time_stamp = int(time.mktime(time_array)) * 1000
        return time_stamp
    except Exception as e:
        print e
    return None