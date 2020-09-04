# Name : Concatenate
# Link : https://www.hackerrank.com/challenges/np-concatenate/problem
# Difficulty : Easy
# Programming language : Python

import numpy

n,m,p = map(int,input().split())

arr1 = []

arr2 = []

for _ in range(int(n)):
    arr1.append(list(map(int, input().split())))

for _ in range(int(m)):
    arr2.append(list(map(int, input().split())))

arr1 = numpy.array(arr1)

arr2 = numpy.array(arr2)

print(numpy.concatenate((arr1, arr2)))
