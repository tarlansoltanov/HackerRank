# Name : Write a function
# Link : https://www.hackerrank.com/challenges/write-a-function/problem
# Difficulty : Medium
# Programming language : Python

def is_leap(year):
    leap = False

    if year % 4 == 0 and year % 100 != 0:
        leap = True
    if year % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))
