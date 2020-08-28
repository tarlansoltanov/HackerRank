# Name : Maximize It!
# Link : https://www.hackerrank.com/challenges/maximize-it/problem
# Difficulty : Hard
# Programming language : Python

from itertools import product
n, m = map(int, input().split())
ans = 0
a = [map(int, input().split()[1:]) for _ in range(n)]
b = [[(j**2) % m for j in a[i]] for i in range(len(a))]
print(max(list(sum(i) % m for i in product(*b))))
