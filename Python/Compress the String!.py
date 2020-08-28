# Name : Compress the String!
# Link : https://www.hackerrank.com/challenges/compress-the-string/problem
# Difficulty : Medium
# Programming language : Python

from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
