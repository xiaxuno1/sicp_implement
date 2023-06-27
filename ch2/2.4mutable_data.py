# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 2.4mutable_data
# Author: xiaxu
# DATA: 2023/6/21
# Description:
# ---------------------------------------------------

"""
手动实现函数式的列表
"""

empty_rlist = None
def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return (first, rest)
def first(s):
    """Return the first element of a recursive list s."""
    return s[0]
def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]

def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist

def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1 #迭代到最后None,就是长度
    return length
def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1 #index从0开始
    return first(s)

def make_mutable_rlist():
    """调度器"""
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist #nonlocal必须要先声明
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)

    return dispatch

def to_mutable_rlist(source):
        """Return a functional list with the same contents as source.
        辅助函数：序列到列表的构建
        """
        s = make_mutable_rlist()
        for element in reversed(source):
            s('push_first', element)
        return s

if __name__ == '__main__':
    suites = ['heart', 'diamond', 'spade', 'club']
    s = to_mutable_rlist(suites)
    print(type(s))
    print(s('str'))