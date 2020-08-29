# Name : Collections.namedtuple()
# Link : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Difficulty : Easy
# Programming language : Python

from collections import namedtuple
n = int(input())
ans = 0
Student = namedtuple('Student', ','.join(input().split()))
for i in range(n):
    k = Student(*input().split())
    ans += int(k.MARKS)
print('{:2f}'.format(ans/n))
