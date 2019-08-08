import datetime

today = datetime.date.today()

# print the date of today
print(today)

# year
print('current year: ', today.year)

# month
print('current month: ', today.month)

# day
print('current day: ', today.day)

# create a date
ind_day = datetime.date(1945, 8, 17)

print(ind_day)

# print now date and time
print(datetime.datetime.now())

# create a time
my_time = datetime.time(13, 23, 45)

print(my_time)

print('the hour: ', my_time.hour)

# create date and time at the same time using same class
my_date_time = datetime.datetime(2000, 2, 28, 15, 29, 58)

print(my_date_time)


# last week date
last_week = datetime.date.today() - datetime.timedelta(days=7)

print(last_week)

# create a timedelta

delta = datetime.timedelta(weeks=1, days=3)

print('total different to today: ', delta.days)

print('total seconds in different: ', delta.total_seconds())

print('total minutes in different: ', (delta.total_seconds()/60))

# format a date
print(today.strftime('%m-%d-%Y'))


