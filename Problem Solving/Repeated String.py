# Name : Repeated String
# Link : https://www.hackerrank.com/challenges/repeated-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys
from collections import Counter


def repeatedString(s, n):
    l = len(s)
    sc = Counter(s)
    m = sc['a']
    ans = n//l*m
    if n % l != 0:
        ans += s[:n % l].count('a')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
