class Money:
    EXCHANGE = {'USD': 430, 'RUS': 6.45}
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

    def __str__(self):
        return f'{self.value} {self.currency}'

    def __add__(self, other):
        x = self.value
        if self.currency == other.currency:
            x += other.value
        else:
            rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]
            x += (rate * other.value)
        return Money(self.currency, x)

    def __sub__(self, other):
        print('Money sub')
        x = self.value

        if self.currency == other.currency:   #why ?
            x -= other.value

        else:
            rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]
            x -= (rate * other.value)

        if x < 0:
            return False
        return Money(self.currency, x)


m = Money('USD ', 2500)
# print(m)