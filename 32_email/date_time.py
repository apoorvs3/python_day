import datetime as dt
import random

#
now = dt.datetime.now()
# year = now.year
# print(year)
#
# print(type(now))
# print(type(year))
#
# date_of_birth = dt.datetime(year=1996, month=6, day=9, hour=10, minute=20)
# print(date_of_birth)
current_day = now.weekday()
print(current_day)


def select_quote():
    with open('quotes.txt') as data:
        content = data.readlines()
    quote = random.choice(content)
    return quote
