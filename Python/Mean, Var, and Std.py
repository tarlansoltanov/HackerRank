# Name : Mean, Var, and Std
# Link : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = []

n, m = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

numpy.set_printoptions(legacy='1.13')

print(numpy.mean(arr, axis=1))

print(numpy.var(arr, axis=0))

print(numpy.std(arr))
