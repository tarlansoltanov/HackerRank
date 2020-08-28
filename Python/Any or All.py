# Name : Any or All
# Link : https://www.hackerrank.com/challenges/any-or-all/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(all([i > 0 for i in arr]) and any(
    [list(reversed(list(str(i)))) == list(str(i)) for i in arr]))
