# Name : itertools.permutations()
# Link : https://www.hackerrank.com/challenges/itertools-permutations/problem
# Difficulty : Easy
# Programming language : Python

from itertools import permutations
s, n = input().split(" ")
ans = sorted(list(permutations(s, int(n))))
for i in ans:
    print(''.join(j for j in i))
