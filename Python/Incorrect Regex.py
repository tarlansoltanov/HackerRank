# Name : Incorrect Regex
# Link : https://www.hackerrank.com/challenges/incorrect-regex/problem
# Difficulty : Easy
# Programming language : Python

import re
for i in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
