# Name : Making Anagrams
# Link : https://www.hackerrank.com/challenges/making-anagrams/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def makingAnagrams(s1, s2):
    ans = len(s1 + s2)
    s = set(s1+s2)
    for c in s:
        ans -= min(s1.count(c), s2.count(c))*2
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
