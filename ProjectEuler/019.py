def daysInMonth(year, month):
    if month != 2:
        days = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month - 1]
    else:
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            return 29
        else:
            return 28
days = 1
sundays = 0

for year in range(1900, 2001):
    for month in range(1, 13):
        days += daysInMonth(year, month)
        if year >= 1901 and days % 7 == 0:
            print(year, month, days)
            sundays += 1

print(sundays)