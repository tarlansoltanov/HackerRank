# Name : The Captain's Room
# Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Difficulty : Easy
# Programming language : Python

k = int(input())
l = list(map(int, input().split()))
s = set(l)

print(((sum(s)*k)-sum(l))//(k-1))
