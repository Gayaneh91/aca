# class DateTime:
#     def __init__(self, date, time):
#         self.date = date
#         self.time = time
#
#     def __str__(self):
#         return f'{self.date}, {self.time}'
#
#
#
# dt = DateTime(9, 6)
# print(dt)


# Programmer
class TimeError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Time:
    def __init__(self, h, m, s):
        try:
            if h < 0 or h > 23:
                raise TimeError("Hour", h)
            if m < 0 or m > 59:
                raise TimeError("Minute", m)
            if s < 0 or s > 59:
                raise TimeError("Second", s)
        except TimeError as err:
            print(err)
        else:
            self.__hour = h
            self.__minute = m
            self.__second = s
            # finally:
        #    print("Object creation process")

    def __repr__(self):
        # TODO: add 0 if any value is < 10
        # return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)
        return "{:02d}:{:02d}:{:02d}".format(self.__hour, self.__minute, self.__second)


    def get_second(self):
        return self.__second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute


    def set_hour(self, x):
        if x > 0 and x < 23:
            self.__hour = x
            print('Value successfuly changed')
        else:
            print("Sorry: Invalid value")


    def add_hour(self, h):
        # TODO: check param type
        self.__hour = (self.__hour + h) % 24


    def add_minute(self, m):
        x = self.__minute + m
        self.__minute = x % 60
        self.add_hour(x // 60)


    def add_second(self, s):
        x = self.__second + s
        self.__second = x % 60
        self.add_minute(x // 60)


#User
# t = Time(15, 3, 48)
# t1 = Time(5, 5, 5)
# print(t)
# t1.get_second()
# print(t)


#Programmer
class DateError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y)
            if m < 1 or m > 12:
                raise DateError("Month", m)
            if d < 1 or d > 30:
                raise DateError("Day", d)
        except DateError as err:
            print(err)
        else:
            self.__year = y
            self.__month = m
            self.__day = d

    def __str__(self):
        # return "{}/{}/{}".format(self.__year, self.__month, self.__day)
        return "{:02d}/{:02d}/{:02d}".format(self.__year, self.__month, self.__day)

    # TODO get functions for all data-members

    def add_year(self, y):
        self.__year += y

    def add_month(self, m):
        x = self.__month + m
        self.__month = x % 12
        if self.__month == 0:
            self.__month = 12
        # TODO : what if x == 12?
        self.add_year(x // 12)



    def add_day(self, d):
        x = self.__day + d

        self.__day = x % 30
        if self.__day == 0:
            self.__day = 30
        # TODO : what if x == 30?
        self.add_month(x // 30)



class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)

    def add_year(self, y):
       self.__date.add_year(y)

    def add_month(self, m):
        self.__date.add_month(m)

    def add_day(self, d):
        self.__date.add_day(d)

    def add_minute(self, m):
        self.__time.add_minute(m)

    def add_second(self, s):
        self.__time.add_second(s)

    def add_hour(self, h):
        x = self.__time.get_hour() + h
        self.__time.add_hour(x % 24)
        self.__date.add_day(x // 24)


d = Date(2023, 8, 6)
# print(d)
# t = Time(16, 29, 6)
# print(t)
# dt = DateTime(d, t)
# print(dt)