# Name : Python If-Else
# Link : https://www.hackerrank.com/challenges/py-if-else/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def check(n):
    if n % 2 == 1:
        return "Weird"
    if n in range(2, 5):
        return "Not Weird"
    if n in range(6, 21):
        return "Weird"
    return "Not Weird"


if __name__ == '__main__':
    n = int(input().strip())
    print(check(n))
