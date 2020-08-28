# Name : ginortS
# Link : https://www.hackerrank.com/challenges/ginorts/problem
# Difficulty : Medium
# Programming language : Python

s = input()
lower = [i for i in s if i.islower()]
upper = [i for i in s if i.isupper()]
odd = [i for i in s if i.isdigit() and int(i) % 2 == 1]
even = [i for i in s if i.isdigit() and int(i) % 2 == 0]
ans = sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)
print(''.join(i for i in ans))
