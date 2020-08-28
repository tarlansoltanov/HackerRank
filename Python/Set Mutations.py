# Name : Set Mutations
# Link : https://www.hackerrank.com/challenges/py-set-mutations/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, m = input().split()
    k = set(map(int, input().split()))
    eval("s." + cmd + "(k)")
print(sum(s))
