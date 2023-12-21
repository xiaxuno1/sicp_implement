# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: stream
# Author: xiaxu
# DATA: 2023/6/28
# Description:
# ------------------------------------------------

"""
`Stream`的剩余部分还是`Stream`。流的剩余部分只在查找时被计算，而不是事先存储。也就是说流的剩余部分是惰性计算的。
为了完成这个惰性求值，流会储存计算剩余部分的函数。无论这个函数在什么时候调用，它的返回值都作为流的一部分，储存在叫做`_rest`的属性中
"""
class Stream(object):
    """A lazily computed recursive list."""
    def __init__(self, first, compute_rest, empty=False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest
    def __repr__(self):
        if self.empty:
            return '<empty stream>'
        return 'Stream({0}, <compute_rest>)'.format(repr(self.first))
