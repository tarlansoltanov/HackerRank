# Name : Detect Floating Point Number
# Link : https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Difficulty : Easy
# Programming language : Python

import re

for _ in range(int(input())):
    s = input()
    x = re.fullmatch(r'^([+-.])?([0-9]+)?\.[0-9]+', s)
    print(True if x != None else False)
