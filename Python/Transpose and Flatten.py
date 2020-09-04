# Name : Transpose and Flatten
# Link : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = []

a, n = input().split()

for _ in range(int(a)):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())
