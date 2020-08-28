# Name : CamelCase
# Link : https://www.hackerrank.com/challenges/camelcase/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def camelcase(s):
    ans = 1
    for i in s:
        if ord(i) < 97:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
