# Name : Re.split()
# Link : https://www.hackerrank.com/challenges/re-split/problem
# Difficulty : Easy
# Programming language : Python

import re
regex_pattern = r"[.,]"

print("\n".join(re.split(regex_pattern, input())))
