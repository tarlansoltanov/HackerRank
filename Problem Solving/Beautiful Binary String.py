# Name : Beautiful Binary String
# Link : https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    i = 0
    ans = 0
    while i < len(b):
        if b[i:i+3] == '010':
            ans += 1
            i += 3
            continue
        i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
