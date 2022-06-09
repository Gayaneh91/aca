# print('There will be my homework.'
# from person import Person
# from money import Money
# from date_time import DateTime
import random
from datetime import date
import string
from date_time import Date
from money import Money
from person import Person


class BankAccount:
    def __init__(self, p : 'Person', m: 'Money', d: 'Date') -> None:
        self.__customer = p
        self.__account_number = ''.join(random.choices(string.digits, k = 16))
        self.__balance = m
        self.__valid_till = d
        #TODO: add other data members if you need

    def __str__(self):
        return f'{self.__customer}\nCard number - {self.__account_number}\nAccount balance - {self.__balance}' \
               f'\nValid till - {self.__valid_till}'

    def get__customer(self):
         return self.__customer

    def get__account_number(self):
        return self.__account_number

    def get__balance(self):
        return self.__balance

    def get__valid_till(self):
        return self.__valid_till

    def set__customer(self, x):
        self.__customer = p

    def set__account_number(self, x):
        self.__account_number = x

    def set__balance(self, m):
        self.__balance = m

    def set__valid_till(self, d):
        self.__valid_till = d

    def deal(self, m):
        #TODO: make transaction , check if balance is enough
        x = self.__balance - m

        if x:
            self.__balance = x
            print('Deal approved. Your current balance is' '-' f'{x}')
        else:
            print('Sorry:( Balance is not enough.')

    def fill_balance(self, m):
        #TODO: fill your balance
        self.__balance += m

        print('Congratulations! Balance successfully filled. Your current balance is' '-' f'{self.__balance}')

    def deposite(self, m, d, p):
        # money, duration, percent
        # TODO: count money after duration with p percent
        n = 0
        if self.__balance - m:
            n = m * ((1 + p/100)**d)

        print("Your balance after {} with percent {} will be {}".format(d, p, self.__balance - m + n))


    def update(self, n):
        self.__valid_till.add_year(2)

p = Person('Gag', 'Grigoryan', 'Male', 18, 'AD235689')
m = Money('USD', 2500)
d = Date(2023, 8, 6)

ba = BankAccount(p, m, d)
#print(ba)
#ba.fill_balance(m)
vt = Date(2024, 6, 8)
m_1 = Money('USD', 2000)
#ba.deal(m_1)
#ba.fill_balance(m)
ba.deposite(m_1, 10, 10)



