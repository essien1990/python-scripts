import calendar

print('========================Calendar===============================')
# week header
print(calendar.weekheader(4))
print()

# week
print(calendar.firstweekday())
print()

# month(year, month)
print(calendar.month(2021, 4, w=0, l=0))
print()

# month display in array
print(calendar.monthcalendar(2021, 1))
print()

# full calendar
print(calendar.calendar(2021))
