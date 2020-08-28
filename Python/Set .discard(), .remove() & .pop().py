# Name : Set .discard(), .remove() & .pop()
# Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    cmd = input()
    if cmd != "pop":
        k = cmd.split(" ")
        cmd = k[0] + "(" + k[1] + ")"
    else:
        cmd += "()"
    eval("s.{}".format(cmd))
print(sum(s))
