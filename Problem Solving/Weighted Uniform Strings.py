# Name : Weighted Uniform Strings
# Link : https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

s = input()
n = int(input())
scores = set()
count = 1
for i in range(len(s)):
    count = count+1 if (i+1 != len(s) and s[i+1] == s[i]) else 1
    scores.add((ord(s[i])-96)*count)

for _ in range(n):
    x = int(input())
    print("Yes" if x in scores else "No")
