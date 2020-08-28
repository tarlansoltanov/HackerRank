# Name : Day 3: Intro to Conditional Statements
# Link : https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys


def check(n):
    if n % 2 == 1:
        return "Weird"
    elif n in range(6, 21):
        return "Weird"
    return "Not Weird"


if __name__ == '__main__':
    N = int(input())
    print(check(N))
