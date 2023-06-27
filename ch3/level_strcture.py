# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 3.3level_strcture
# Author: xiaxu
# DATA: 2023/6/26
# Description:层次结构
# ---------------------------------------------------
from numpy import square


def map_tree(tree, fn): #映射和递归一起为树的操作提供了强大而通用的计算形式
    if type(tree) != tuple:
        return fn(tree)  #映射的函数
    return tuple(map_tree(branch, fn) for branch in tree) #递归

def count_leaves(tree,leaves = 0):
    def counts(tree):
        nonlocal leaves  #非局部变量，用于存储和更新leaves
        if type(tree)!= tuple:
            leaves = leaves+1
            return leaves #迭代的结束标志
        tuple(counts(branch) for branch in tree) #迭代的计算式：一步一步减少列表的深度
        return leaves
    return counts(tree)

#另一个通用的树形结构表示也在树的内部节点上存在值.`Tree`类可以为`fib`的递归实现表示表达式树中计算的值。`fib`函数用于计算斐波那契数。
# 下面的函数`fib_tree(n)`返回`Tree`，它将第 n 个斐波那契树作为`entry`，并将所有之前计算出来的斐波那契数存入它的枝干中。
class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

def fib_tree(n):
    """Return a Tree that represents a recursive Fibonacci calculation."""
    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    return Tree(left.entry + right.entry, left, right)

if __name__ == '__main__':
    t = ((1, 2), 3, 4)
    big_tree = ((t, t), 5)
    print(map_tree(big_tree, square))
    print(count_leaves(big_tree))
    fib_tree(10)