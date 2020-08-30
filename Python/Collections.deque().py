# Name : Collections.deque()
# Link : https://www.hackerrank.com/challenges/py-collections-deque/problem
# Difficulty : Easy
# Programming language : Python

from collections import deque
n = int(input())
arr = deque()
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        eval(f'arr.{cmd[0]}(cmd[1])')
    else:
        eval(f'arr.{cmd[0]}()')
print(' '.join(arr))
