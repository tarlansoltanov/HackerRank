# Name : Sum and Prod
# Link : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = []

n, m = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

arr = numpy.sum(arr, axis=0)

print(numpy.prod(arr))
