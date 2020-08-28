# Name : Day 4: Class vs. Instance
# Link : https://www.hackerrank.com/challenges/30-class-vs-instance/problem
# Difficulty : Easy
# Programming Language : Python

class Person:
    def __init__(self, initialAge):
        age = initialAge
        if age < 0:
            print("Age is not valid, setting age to 0.")
            age = 0

    def amIOld(self):
        if age < 13:
            print("You are young.")
        elif age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        global age
        age += 1
