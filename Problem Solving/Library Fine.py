# Name : Library Fine
# Link : https://www.hackerrank.com/challenges/library-fine/problem
# Difficulty : Easy
# Programming language : Python

r = list(map(int, input().split()))
e = list(map(int, input().split()))


def solution(r, e):
    if r[2] < e[2]:
        return 0
    if r[2] == e[2]:
        if r[1] < e[1]:
            return 0
        if r[1] == e[1]:
            if r[0] < e[0]:
                return 0
            if r[0] == e[0]:
                return 0
            return (r[0]-e[0])*15
        return (r[1]-e[1])*500
    return 10000


print(solution(r, e))
