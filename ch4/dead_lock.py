# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: dead_lock
# Author: xiaxu
# DATA: 2023/6/28
# Description:
# ---------------------------------------------------
from threading import Lock

x_lock = Lock()
y_lock = Lock()
x = 1
y = 0
def compute():
    x_lock.acquire()
    y_lock.acquire()
    y = x + y
    x = x * x
    y_lock.release()
    x_lock.release()
def anti_compute():
    y_lock.acquire()
    x_lock.acquire()
    y = y - x
    x = sqrt(x)
    x_lock.release()
    y_lock.release()