# Name : Iterables and Iterators
# Link : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Difficulty : Medium
# Programming language : Python

from itertools import combinations
n = int(input())
arr = input().split()
m = int(input())
ans = []
for i in range(len(arr)):
    if arr[i]=='a':
        ans.append(i)

poss = list(combinations([i for i in range(n)],m))

k = 0

for i in poss:
    for elem in i:
        if elem in ans:
            k+=1
            break

print('{:4f}'.format(k/len(poss)))
    
