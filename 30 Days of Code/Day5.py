# Name : Day 5: Loops
# Link : https://www.hackerrank.com/challenges/30-loops/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)
