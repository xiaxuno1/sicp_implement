# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 3.3set_container
# Author: xiaxu
# DATA: 2023/6/26
# Description:集合
# ---------------------------------------------------
from ch3.recursive_data_structure import Rlist


#将集合作为无需序列，利用Rlist实现
def empty(s):
    return s is Rlist.empty
def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    return set_contains(s.rest, v) #迭代判断集合内数据是否存在
#添加到集合，并返回
def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    return Rlist(v, s)
#求交集并集时可能时间复杂度为     O(n^2)


if __name__ == '__main__':
    s = Rlist(1,Rlist(2,Rlist(3)))
    print(set_contains(s, 2))#True
    print(set_contains(s,5))#Flase
    print(adjoin_set(s, 5))