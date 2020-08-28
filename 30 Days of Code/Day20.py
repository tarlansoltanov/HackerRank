# Name : Day 20: Sorting
# Link : https://www.hackerrank.com/challenges/30-sorting/problem
# Difficulty : Easy
# Programming Language : Python

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
ans = 0
for i in range(len(a)):
    k = 0
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            k += 1
            a[j], a[j+1] = a[j+1], a[j]
    ans += k
    if k == 0:
        break

print(f'Array is sorted in {ans} swaps.\n'
      f'First Element: {a[0]}\n'
      f'Last Element: {a[len(a)-1]}')
