# Name : collections.Counter()
# Link : https://www.hackerrank.com/challenges/collections-counter/problem
# Difficulty : Easy
# Programming language : Python

from collections import Counter

ans = 0

n = int(input())

arr = map(int, input().split())

arr = Counter(arr)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if arr[x] != 0:
        ans += y
        arr[x] -= 1

print(ans)
