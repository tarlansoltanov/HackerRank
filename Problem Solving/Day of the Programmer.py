# Name : Day of the Programmer
# Link : https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def dayOfProgrammer(year):
    if year == 1918:
        return("26.09.1918")
    if year % 4 == 0:
        if (year < 1918) or (year > 1918 and (year % 400 == 0 or year % 100 != 0)):
            return("12.09." + str(year))
    return("13.09." + str(year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
