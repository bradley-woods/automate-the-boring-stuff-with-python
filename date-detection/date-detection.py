# Automate the Boring Stuff with Python
# Chapter 7 - Pattern Matching with Regular Expressions: Date Detection

import re

date = '22/05/2023'

dateRegex = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([12][0-9][0-9][0-9])')

if dateRegex.search(date):
    day = date.split('/')[0]
    month = date.split('/')[1]
    year = date.split('/')[2]

    # Check for leap year which has 29 days in February
    if int(year) % 4 == 0:
        if int(year) % 400 == 0:
            days = 29
        elif int(year) % 100 == 0:
            days = 28
        else:
            days = 29
    else:
        days = 28

    if month == "02" and int(day) > days:
        print("Invalid date")
    elif month in ["04", "06", "09", "11"] and int(day) > 30:
        print("Invalid date")
    else:
        print(f"{day}/{month}/{year} is valid")

else:
    print("Invalid date")