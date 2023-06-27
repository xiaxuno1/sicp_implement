# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: calculator
# Author: xiaxu
# DATA: 2023/6/26
# Description:计算器
# ---------------------------------------------------

class Exp(object):
    """A call expression in Calculator.
    表达式树,用于实现表达式的嵌套形式
    """
    def __init__(self, operator, operands):
        self.operator = operator #算术运算符的字符串
        self.operands = operands #表达式
    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))
    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

#求值
def calc_eval(exp):
    """Evaluate a Calculator expression.
    `calc_eval`的作用是，执行合适的`calc_apply`调用，
    通过首先计算操作数子表达式的值，之后将它们作为参数传入`calc_apply`。于是，`calc_eval`可以接受嵌套表达式。
    """
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands)) #递归调用解除嵌套，不断对operands调用calc_eval
        return calc_apply(exp.operator, arguments)

from operator import mul
from functools import reduce
def calc_apply(operator, args):
    """Apply the named operator to a list of args.
    >>> calc_apply('+', [1, 2, 3])
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom

#REPL它打印出对由`calc_parse`返回的表达式树调用`calc_eval`的结果。
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> ')) #调用字符串解析器，返回Exp(op,operend)
            print(calc_eval(expression_tree)) #调用计算表达式树
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return

"""
解析是从原始文本输入生成表达式树的过程。解释这些表达式树是求值函数的任务，但是解析器必须提供符合格式的表达式树给求值器。
解析器实际上由两个组件组成，词法分析器和语法分析器。首先，词法分析器将输入字符串拆成标记（token），它们是语言的最小语法单元，
就像名称和符号那样。其次，语法分析器从这个标记序列中构建表达式树。
这里，我们定义了`calc_parse`，它只接受符合格式的计算器表达式
**词法分析。**用于将字符串解释为标记序列的组件叫做分词器（tokenizer ），或者词法分析器。
**语法分析。**将标记序列解释为表达式树的组件叫做语法分析器。
"""
def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line) #将字符串分开
    expression_tree = analyze(tokens) #将分开的字符串，分析为表达式树
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens.分词器，将输入的字符串分割"""
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ')
    return spaced.split()

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.语法分析，将分词器的内容分析为表达式树"""
    token = analyze_token(tokens.pop(0))#取出每个内容，分析为数值还是其他
    if type(token) in (int, float):
        return token
    else: #不是数值的情况，就是操作符，后面是（oprend）
        tokens.pop(0)  # Remove (
        return Exp(token, analyze_operands(tokens)) #返回成表达式树，（opreater,oprand）

def analyze_operands(tokens):
    """Read a list of comma-separated operands.组成operand列表 eg[1, Exp('mul', [2, 3, 4]"""
    operands = []
    while tokens[0] != ')': #括号表示结束
        if operands:
            tokens.pop(0)  # Remove ,
        operands.append(analyze(tokens)) #递归返回数值
    tokens.pop(0)  # Remove )
    return operands

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.`analyze_token`函数将数值文本转换为数值。
    其他返回原数据"""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


if __name__ == '__main__':
    print(Exp('add', [1, 2]))
    print(str(Exp('add', [1, 2])))
    e = Exp('add', [1, Exp('mul', [2, 3, 4])])
    print(str(e))#add(1, mul(2, 3, 4))
    print(calc_apply('+', [1, 2, 3]))
    calc_eval(e)
    read_eval_print_loop()

