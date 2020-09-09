# Name : Chocolate Feast
# Link : https://www.hackerrank.com/challenges/chocolate-feast/problem
# Difficulty : Easy
# Programming language : Python


import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    ans = n//c
    k = n//c
    while k >= m:
        ans += 1
        k -= (m-1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
