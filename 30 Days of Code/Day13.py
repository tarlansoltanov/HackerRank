# Name : Day 13: Abstract Classes
# Link : https://www.hackerrank.com/challenges/30-abstract-classes/problem
# Difficulty : Easy
# Programming Language : Python

class MyBook():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))
