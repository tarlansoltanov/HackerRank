# Name : Palindrome Index
# Link : https://www.hackerrank.com/challenges/palindrome-index/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def check(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


def palindromeIndex(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            if check(s[:i]+s[i+1:]):
                return i
            return len(s)-1-i
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
