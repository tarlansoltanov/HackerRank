# Name : Day 7: Arrays
# Link : https://www.hackerrank.com/challenges/30-arrays/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(' '.join(str(i) for i in list(reversed(arr))))
