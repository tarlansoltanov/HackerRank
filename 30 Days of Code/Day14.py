# Name : Day 14: Scope
# Link : https://www.hackerrank.com/challenges/30-scope/problem
# Difficulty : Easy
# Programming Language : Python


class Difference:
    def __init__(self, a):
    self.__elements = a


def computeDifference(self):
    self.maxx = int(max(self.__elements))
    self.minn = int(min(self.__elements))
    self.maximumDifference = int(self.maxx-self.minn)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
