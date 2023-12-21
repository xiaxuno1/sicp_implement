# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: coroutine
# Author: xiaxu
# DATA: 2023/6/28
# Description:协程
# ---------------------------------------------------
import time


def match(pattern):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield) #等待接收send产生的值
            if pattern in s:
                print(s)
    except GeneratorExit:
        print("=== Done ===")


if __name__ == '__main__':
    m=match('1234')
    m.__next__() #Looking for 1234
    time.sleep(3)
    m.send('1234567890')#1234567890
    m.close()  #关闭协程，实际上是产生GneratorExit异常，然后被捕获，打印done

