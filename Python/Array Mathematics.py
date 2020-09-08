# Name : Array Mathematics
# Link : https://www.hackerrank.com/challenges/np-array-mathematics/problem
# Difficulty : Easy
# Programming language : Python

import numpy

n, m = map(int, input().split())

arr1 = []

for _ in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []

for _ in range(n):
    arr2.append(list(map(int, input().split())))

a = numpy.array(arr1, int)
b = numpy.array(arr2, int)


ans = numpy.array(a+b, int)
print(ans)
ans = numpy.array(a-b, int)
print(ans)
ans = numpy.array(a*b, int)
print(ans)
ans = numpy.array(a/b, int)
print(ans)
ans = numpy.array(a % b, int)
print(ans)
ans = numpy.array(a**b, int)
print(ans)
