# Name : Jumping on the Clouds: Revisited
# Link : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    ans = 100
    m = 0
    while m+k != len(c):
        m += k
        if m > len(c):
            m -= len(c)
        ans -= 1
        if c[m] == True:
            ans -= 2

    return(ans-1 if c[0] == 0 else ans-3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
