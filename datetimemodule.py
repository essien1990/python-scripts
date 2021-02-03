import datetime
import pytz

today = datetime.date.today()
print(today)

print()

birthday = datetime.date(1990, 7, 5)
print(birthday)


print()

# find day since birth
days_since_birthday = (today - birthday).days
print(days_since_birthday)


print()

# adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print()

print(today.day)

#Thursday = 3
print(today.weekday())

print()

print(datetime.time(5, 29, 15, 20))
# datatime.date(Y, D M)
# datettime.time(h,m,s,ms)
# datetime.datetime(Y,M,D,h,m,s,ms)

print()

# Add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

# Time Zones
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Africa/Accra'))
print(datetime_pacific)

# printing all time Zones
for tz in pytz.all_timezones:
    print(tz)
print()

# String formatting for dates
# 2019-03-09 -> March 3, 2019
# %B->Month, %d->day, %Y->year
# strftime (f=formating)
print()
print(datetime_pacific.strftime('%B %d, %Y'))

# March 09, 2019 -> datetime(2019,03,09)
# strptime (p=parsing)

print(repr(datetime.datetime.strptime('March 09, 2020', '%B %d, %Y')))
