# Name : DefaultDict Tutorial
# Link :https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Difficulty : Easy
# Programming language : Python

from collections import defaultdict

n, m = map(int, input().split())

ans = defaultdict(list)

for i in range(1, n+1):
    l = input()
    ans[l].append(i)

for i in range(m):
    l = input()
    if ans[l]:
        print(' '.join(str(j) for j in ans[l]))
    else:
        print(-1)
