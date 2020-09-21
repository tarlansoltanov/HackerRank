# Name : Encryption
# Link : https://www.hackerrank.com/challenges/encryption/problem
# Difficulty : Medium
# Programming language : Python

import math
import os
import random
import re
import sys


def encryption(s):
    r = math.floor(len(s)**0.5)
    c = math.ceil(len(s)**0.5)
    if r*c < len(s):
        r = c
    ans = ""
    for i in range(c):
        j = i
        while j < len(s):
            ans += s[j]
            j += c
        ans += " "
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
