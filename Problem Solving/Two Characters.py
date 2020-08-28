# Name : Two Characters
# Link : https://www.hackerrank.com/challenges/two-characters/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def valid(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


def alternate(s):
    if len(s) == 1:
        return 0
    ss = set(s)
    ans = 0
    for i in ss:
        for x in ss:
            arr = [c for c in s if c == i or c == x]
            if valid(arr):
                ans = max(ans, len(arr))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
