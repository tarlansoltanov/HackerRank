# Name : Anagram
# Link : https://www.hackerrank.com/challenges/anagram/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def anagram(s):
    if len(s) % 2 == 1:
        return -1
    ans = 0
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    for i in set(s2):
        k = s2.count(i)-s1.count(i)
        if k > 0:
            ans += k
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
