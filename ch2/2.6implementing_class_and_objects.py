# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 2.6实现类和对象
# Author: xiaxu
# DATA: 2023/6/21
# Description:
# ---------------------------------------------------
def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance
"""
**绑定方法值。**`make_instance`中的`get_value `使用`get`寻找类中的具名属性，之后调用`bind_method`。方法的绑定只在函数值上调用，
并且它会通过将实例插入为第一个参数，从函数值创建绑定方法的值。
"""
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value