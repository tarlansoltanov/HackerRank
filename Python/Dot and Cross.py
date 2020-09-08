# Name : Dot and Cross
# Link : https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr1 = []

arr2 = []

n = int(input())

numpy.set_printoptions(legacy='1.13')

for _ in range(n):
    arr1.append(list(map(int, input().split())))

arr1 = numpy.array(arr1)

for _ in range(n):
    arr2.append(list(map(int, input().split())))

arr2 = numpy.array(arr2)

print(numpy.dot(arr1, arr2))
