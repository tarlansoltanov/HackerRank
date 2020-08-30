# Name : Company Logo
# Link : https://www.hackerrank.com/challenges/most-commons/problem
# Difficulty : Medium
# Programming language : Python

from collections import Counter

myDict = Counter(input()).items()

for key, value in sorted(myDict, key=lambda c: (-c[1], c[0]))[:3]:
    print(key, value)
