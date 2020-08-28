# Name : Jumping on the Clouds
# Link : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    jump = 0
    n = 0
    while n < len(c)-2:
        if c[n+2] == 0:
            n += 2
        else:
            n += 1
        jump += 1
    if n != len(c)-1:
        jump += 1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
