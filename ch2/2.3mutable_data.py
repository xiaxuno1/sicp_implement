# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: 2.3mutable_daa
# Author: xiaxu
# DATA: 2023/6/21
# Description:可变数据
# ---------------------------------------------------

'''
局部状态
我们会通过创建叫做`withdraw`的函数来实现它，它将要取出的金额作为参数。如果账户中有足够的钱来取出，
`withdraw`应该返回取钱之后的余额。否则，`withdraw`应该返回消息`'Insufficient funds'`。
'''
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""

    def withdraw(amount):
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount  # Re-bind the existing balance name
        return balance

    return withdraw

if __name__ == '__main__':
    withdraw = make_withdraw(100)
    #每次会更新balance的值
    print(withdraw(20))#80
    print(withdraw(15))#65