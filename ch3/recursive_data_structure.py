# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 3.3递归数据结构
# Author: xiaxu
# DATA: 2023/6/26
# Description:递归数据结构
# ---------------------------------------------------



"""
递归函数实现列表的抽象
"""
class Rlist(object):
    """A recursive list consisting of a first element and the rest."""

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()  #这是一个类属性，通过类名。属性名调用；不需要创建对象

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):#递归调用
        return 1 + len(self.rest)

    def __getitem__(self, i):#递归调用rest[]会默认调用_getitem__
        if i == 0:
            return self.first
        return self.rest[i - 1]

#创建新列表，接收两个递归列表组合成为新的列表
def extend_rlist(s1, s2):
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))




if __name__ == '__main__':
    s = Rlist(1,Rlist(2,Rlist(3)))
    s.rest#打印对象会打印其内建函数__repr__
    print(len(s))#调用len会默认调用内建函数__len__
    print(s[1])#下标迭代会默认

    extend_rlist(s.rest, s)
