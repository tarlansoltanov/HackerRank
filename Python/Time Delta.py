# Name : Time Delta
# Link : https://www.hackerrank.com/challenges/python-time-delta/problem
# Difficulty : Medium
# Programming language : Python

import math
import os
import random
import re
import sys
from dateutil import parser


def time_delta(t1, t2):
    date1 = parser.parse(t1)
    date2 = parser.parse(t2)
    return(str(abs(int((date2-date1).total_seconds()))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
