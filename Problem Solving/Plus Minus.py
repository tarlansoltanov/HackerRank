# Name : Plus Minus
# Link : https://www.hackerrank.com/challenges/plus-minus/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def plusMinus(arr):
    ans = [0, 0, 0]
    for i in arr:
        ans[0] += (i > 0)
        ans[1] += (i < 0)
        ans[2] += (i == 0)
    print('{:6f}'.format(ans[0]/len(arr)))
    print('{:6f}'.format(ans[1]/len(arr)))
    print('{:6f}'.format(ans[2]/len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
