# print('There will be my homework.'
# from person import Person
# from money import Money
# from date_time import DateTime
import random

from classwork.date_time import dt
from classwork.money import m
from classwork.person import p


class BankAccount:
    def __init__(self, p : 'Person', m: 'Money', d: 'DateTime'): #-> None
        self.customer = p
        self.account_number = [random.randint(0, 50) for _ in range(16)]   #TODO: generate random 16-len string from digits
        self.balance = m
        self.valid_till = d
        self.m = None
        self.d = None
        self.p = None
        #TODO: add other data members if you need

    def __str__(self):
        return f'{self.customer}\nCard number - {self.account_number}\nAccount balance - {self.balance}' \
               f'\nValid till - {self.valid_till}'

    def deal(self, m):
        #TODO: make transaction , check if balance is enough
        if self.balance > 0:
            self.balance -= self.m

    def fill_balance(self, m):
        #TODO: fill your balance
        self.balance += m

    def deposite(self, m, d, p):
        # money, duration, percent
        # TODO: count money after duration with p percent
        x = self.balance - self.m
        self.d = x + self.m
        self.p = (self.d / self.balance) * 100

ba = BankAccount(p, m, dt)
# ba.deposite(200, 6, 9)
print(ba)

