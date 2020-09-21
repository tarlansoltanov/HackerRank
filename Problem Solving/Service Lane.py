# Name : Service Lane
# Link : https://www.hackerrank.com/challenges/service-lane/problem
# Difficulty : Easy
# Programming language : Python


import math
import os
import random
import re
import sys


def serviceLane(arr, cases):
    ans = []
    for a, b in cases:
        ans.append(min(width[a:b+1]))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
