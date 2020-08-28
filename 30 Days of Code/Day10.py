# Name : Day 10: Binary Numbers
# Link : https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    n = str(bin(n))
    count = 0
    ans = 0
    for i in range(len(n)):
        if n[i] == "1":
            count += 1
        elif n[i] == "0":
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)
