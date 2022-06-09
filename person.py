class Person:
    def __init__(self, fn, ln, a, g, p):
        self.fn = fn
        self.ln = ln
        self.a = a
        self.g = g
        self.p = p

    def __str__(self):
        return f'{self.fn} {self.ln} - {self.g}, {self.a}, {self.p}'

p = Person('Gag', 'Grigoryan', 'Male', 18, 'AD235689')
# print(p)
