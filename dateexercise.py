import datetime

posted_time = datetime.time(hour=10, minute=30, second=0)

now = datetime.datetime.now()

now_time = datetime.time(now.hour, now.minute, now.second)

delta = now_time.hour - posted_time.hour

if delta >= 1:
    print("{0} hours ago".format(delta))
else:
    print("{0} minutes ago".format(now_time.minute - posted_time.minute))

