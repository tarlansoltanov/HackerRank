# Name : Finding the percentage
# Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Difficulty : Easy
# Programming language : Python

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ans = sum(e for e in student_marks[query_name])
    print("{:.2f}".format(ans/len(student_marks[query_name])))
