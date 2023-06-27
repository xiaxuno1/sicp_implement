# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 2.2sequences
# Author: xiaxu
# DATA: 2023/6/21
# Description:
# ---------------------------------------------------

"""
实现嵌套
(1, (2, (3, (4, None))))
这两个选择器和一个构造器，以及一个常量共同实现了抽象数据类型的递归列表。
递归列表唯一的行为条件是，就像偶对那样，它的构造器和选择器是相反的函数。
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
#实现递归嵌套的数据抽象
counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))
#长度和元素选择
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

if __name__ == '__main__':
    print(first(counts)) #1
    print(rest(counts)) # (2, (3, (4, None)))
    print(len_rlist(counts))#4
    print(getitem_rlist(counts,1))#2