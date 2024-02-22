#1

from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print(current_date)
print(new_date)

#2

from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(yesterday)
print(current_date)
print(tomorrow)

#3

from datetime import datetime

current_datetime = datetime.now()

current_datetime = current_datetime.replace(microsecond=0)

print(current_datetime)

#4

from datetime import datetime

date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 22, 12, 0, 0)

difference_seconds = abs((date2 - date1).total_seconds())

print(difference_seconds)
