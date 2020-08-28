# Name : Day 28: RegEx, Patterns, and Intro to Databases
# Link : https://www.hackerrank.com/challenges/30-regex-patterns/problem
# Difficulty : Medium
# Programming Language : Python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    ans = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        x = re.search("@gmail.com", emailID)
        if x != None:
            ans.append(firstName)
    ans.sort()
    print('\n'.join(ans))
