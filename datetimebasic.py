import datetime

# from datetime import date

today = datetime.date.today()

print(today)

year = today.year
month = today.month
day = today.day

print('today year is', year)

# create a date
independence_day = datetime.date(2019, 8, 17)

print(independence_day)

# date and time

now = datetime.datetime.now()

print(now)

future_date_time = datetime.time(13, 56, 45)

print(future_date_time)

print('-' * 20)

delta = independence_day - datetime.date.today()

print(delta.days/30)

print('which is {0} seconds'.format(delta.total_seconds()))


one_week = datetime.timedelta(weeks=1)
next_week = today + one_week


# check http://strftime.org for complete format encoding
print(next_week.strftime('%a %d, %Y'))

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

input_my_day = input('enter a birthday in m-d-yyyy: ')

my_day = datetime.datetime.strptime(input_my_day, '%m-%d-%Y')

print(my_day)

print('the day is %sth of the week' % my_day.weekday())

print('the day is %sth of the week in iso format' % my_day.isoweekday())

print('you were born on', days[my_day.weekday()])





