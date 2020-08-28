# Name : itertools.combinations_with_replacement()
# Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Difficulty : Easy
# Programming language : Python

from itertools import combinations_with_replacement
s, n = input().split(" ")
ans = sorted(list(combinations_with_replacement(sorted(s), int(n))))
for i in ans:
    print(''.join(j for j in i))
