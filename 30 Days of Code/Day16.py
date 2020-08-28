# Name : Day 16: Exceptions - String to Integer
# Link : https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# Difficulty : Easy
# Programming Language : Python

import sys

S = input().strip()

try:
    print(int(S))
except:
    print("Bad String")
