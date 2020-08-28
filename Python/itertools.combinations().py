# Name : itertools.combinations()
# Link : https://www.hackerrank.com/challenges/itertools-combinations/problem
# Difficulty : Easy
# Programming language : Python

from itertools import combinations
s, n = input().split(" ")
s = sorted(s)
for k in range(1, int(n)+1):
    ans = sorted(list(combinations(s, k)))
    for i in ans:
        print(''.join(j for j in i))
