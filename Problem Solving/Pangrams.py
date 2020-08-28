# Name : Pangrams
# Link : https://www.hackerrank.com/challenges/pangrams/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def pangrams(s):
    a = set()
    for i in s:
        if i.isalpha():
            a.add(i.lower())
    print(len(a))
    if len(a) == 26:
        return "pangram"
    return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
