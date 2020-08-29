# Name : Collections.OrderedDict()
# Link : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Difficulty : Easy
# Programming language : Python

from collections import OrderedDict
myDict = OrderedDict()

for i in range(int(input())):
    x = input().split()
    name = ' '.join(x[:len(x)-1])
    price = int(x[len(x)-1])
    if name in myDict.keys():
        myDict[name] += int(price)
    else:
        myDict[name] = int(price)
for key, value in myDict.items():
    print(key, value)
