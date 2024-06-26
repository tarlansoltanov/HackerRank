# Name : Birthday Cake Candles
# Link : https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    return ar.count(max(ar))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
