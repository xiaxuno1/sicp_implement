# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: generic_opration
# Author: xiaxu
# DATA: 2023/6/25
# Description:泛用方法；复数的两种表现的方法
# ---------------------------------------------------
from math import atan2
class ComplexRI(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)

from math import sin, cos
class ComplexMA(object):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    #Python 拥有一个简单的特性，用于从零个参数的函数凭空计算属性（Attribute）。`@property`装饰器允许函数不使用标准调用表达式语法来调用。
    #@property装饰器将返回值设置为属性，可以像属性调用
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)

def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


from math import gcd
class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom) #最大公约数
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)  #分子分母分别相乘

#类型分发
def iscomplex(z):
    return type(z) in (ComplexRI, ComplexMA)
def isrational(z):
    return type(z) == Rational


def add_complex_and_rational(z, r):
        return ComplexRI(z.real + r.numer/r.denom, z.imag)

def add(z1, z2):
    """Add z1 and z2, which may be complex or rational."""
    if iscomplex(z1) and iscomplex(z2):
        return add_complex(z1, z2)
    elif iscomplex(z1) and isrational(z2):
        return add_complex_and_rational(z1, z2)
    elif isrational(z1) and iscomplex(z2):
        return add_complex_and_rational(z2, z1)
    else:
        return add_rational(z1, z2)

#通过以字典实现类型分发,增加了拓展灵活性
def type_tag(x):
    return type_tag.tags[type(x)]
def _add(z1, z2):
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)


if __name__ == '__main__':
    from math import pi
    add_complex(ComplexRI(1, 2), ComplexMA(2, pi / 2))
    ComplexRI(1.0000000000000002, 4.0)
    mul_complex(ComplexRI(0, 1), ComplexRI(0, 1))
    ComplexMA(1.0, 3.141592653589793)
    #字典分发实现
    type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat'}
    _add.implementations = {}
    _add.implementations[('com', 'com')] = add_complex
    _add.implementations[('com', 'rat')] = add_complex_and_rational
    _add.implementations[('rat', 'com')] = lambda x, y: add_complex_and_rational(y, x)
    _add.implementations[('rat', 'rat')] = add_rational
    print(add(ComplexRI(1.5, 0), Rational(3, 2)))



