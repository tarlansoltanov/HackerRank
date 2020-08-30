# Name : Word Order
# Link : https://www.hackerrank.com/challenges/word-order/problem
# Difficulty : Medium
# Programming language : Python

from collections import OrderedDict

myDict = OrderedDict()
for _ in range(int(input())):
    key = input()
    if key in myDict.keys():
        myDict[key] += 1
    else:
        myDict[key] = 1
print(len(myDict))
print(' '.join(str(i) for i in myDict.values()))
