# Name : Re.start() & Re.end()
# Link : https://www.hackerrank.com/challenges/re-start-re-end/problem
# Difficulty : Easy
# Programming language : Python

import re

s = input()

k = input()

x = re.search(k, s)

l = 0

count = 0

while x != None:
    count += 1
    start = l+x.start()
    end = l+x.end()-1
    l = end
    if start == end:
        l += 1
    print(f'({start}, {end})')
    x = re.search(k, s[l:])

if count == 0:
    print((-1, -1))
