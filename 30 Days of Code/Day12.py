# Name : Day 12: Inheritance
# Link : https://www.hackerrank.com/challenges/30-inheritance/problem
# Difficulty : Easy
# Programming Language : Python


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.firstName = firstName
        Person.lastName = lastName
        Person.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        average = sum(scores)/len(scores)
        Grade = "T"
        if average >= 90:
            Grade = "O"
        elif average >= 80:
            Grade = "E"
        elif average >= 70:
            Grade = "A"
        elif average >= 55:
            Grade = "P"
        elif average >= 40:
            Grade = "D"
        return Grade
