# Name : Group(), Groups() & Groupdict()
# Link : https://www.hackerrank.com/challenges/re-group-groups/problem
# Difficulty : Easy
# Programming language : Python

import re

s = input().strip()

x = re.search(r'([a-zA-Z0-9])\1+', s)

print(x.group(1) if x != None else -1)
