# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: sicp
# FN: lock_and_single
# Author: xiaxu
# DATA: 2023/6/28
# Description:
# ---------------------------------------------------
from threading import Lock,Thread,Semaphore
def make_withdraw(balance):
    balance_lock = Lock()
    def withdraw(amount):
        nonlocal balance
        # try to acquire the lock
        balance_lock.acquire()
        # once successful, enter the critical section
        if amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(balance)
        # upon exiting the critical section, release the lock
        balance_lock.release()
    return withdraw

#信号量，参考数据库的连接数
db_semaphore = Semaphore(2) # set up the semaphore
database = []
def insert(data):
    db_semaphore.acquire() # try to acquire the semaphore
    database.append(data)  # if successful, proceed
    db_semaphore.release() # release the semaphore


if __name__ == '__main__':
    m = make_withdraw(100)
    t2 = Thread(target=m,args=(100,))
    t1= Thread(target=m,args=(5,))
    t1.start()
    t2.start()
    if t1.is_alive():
        print('Still running')
    else:
        print('Completed')
    insert(7)
    insert(8)
    insert(9)
