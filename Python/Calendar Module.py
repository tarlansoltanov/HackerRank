# Name : Calendar Module
# Link : https://www.hackerrank.com/challenges/calendar-module/problem
# Difficulty : Easy
# Programming language : Python

import calendar as cl

weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY",
            "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

date = list(map(int, input().split()))

print(weekdays[cl.weekday(date[2], date[0], date[1])])
