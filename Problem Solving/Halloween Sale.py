# Name : Halloween Sale
# Link : https://www.hackerrank.com/challenges/halloween-sale/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    ans = 0
    while s >= 0:
        s -= p
        p = max(p-d, m)
        ans += 1
    return max(0, ans-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
