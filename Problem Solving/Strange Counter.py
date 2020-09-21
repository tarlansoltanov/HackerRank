# Name : Strange Counter
# Link : https://www.hackerrank.com/challenges/strange-code/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def strangeCounter(t):
    k = 3
    while t > k:
        t -= k
        k *= 2
    return k-t+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
