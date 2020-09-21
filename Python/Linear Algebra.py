# Name : Linear Algebra
# Link : https://www.hackerrank.com/challenges/np-linear-algebra/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = []

for i in range(int(input())):
    arr.append(list(map(float, input().split())))

print(round(numpy.linalg.det(numpy.array(arr)), 2))
