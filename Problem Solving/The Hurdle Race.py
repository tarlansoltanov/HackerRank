# Name : The Hurdle Race
# Link : https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def hurdleRace(k, height):
    return max(height)-k if max(height)-k >= 0 else 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
