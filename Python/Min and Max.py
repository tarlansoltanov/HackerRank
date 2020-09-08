# Name : Min and Max
# Link : https://www.hackerrank.com/challenges/np-min-and-max/problem
# Difficulty : Easy
# Programming language : Python

import numpy

import numpy

arr = []

n, m = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

arr = numpy.min(arr, axis=1)

print(numpy.max(arr))
