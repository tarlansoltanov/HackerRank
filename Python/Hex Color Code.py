# Name : Hex Color Code
# Link : https://www.hackerrank.com/challenges/hex-color-code/problem
# Difficulty : Easy
# Programming language : Python

import re

x = re.compile(r"(:|,| +)(#[A-Fa-f0-9]{3}|#[A-Fa-f0-9]{6})\b")

ans = []

for _ in range(int(input())):
    arr = x.findall(input())
    for i in arr:
        print(i[1])
