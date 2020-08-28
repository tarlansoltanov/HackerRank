# Name : Find Angle MBC
# Link : https://www.hackerrank.com/challenges/find-angle/problem
# Difficulty : Medium
# Programming language : Python

import math

n = int(input())

m = int(input())

print(str(int(round(math.degrees(math.atan(n/m)), 0)))+'°')
