# Name : Check Strict Superset
# Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Difficulty : Easy
# Programming language : Python

sa = set(map(int, input().split()))
ans = True
for _ in range(int(input())):
    m = set(map(int, input().split()))
    if m == sa:
        ans = False
    elif m & sa != m:
        ans = False
print(ans)
