# Name : Day 19: Interfaces
# Link : https://www.hackerrank.com/challenges/30-interfaces/problem
# Difficulty : Easy
# Programming Language : Python

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        ans = 0
        if n == 1:
            return 1
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                ans += i+(n//i)
        if n/int(n**0.5) == int(n**0.5):
            ans -= int(n**0.5)
        return ans


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
