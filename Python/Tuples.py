# Name : Tuples
# Link : https://www.hackerrank.com/challenges/python-tuples/problem
# Difficulty : Easy
# Programming language : Python

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(int(i) for i in integer_list)
    print(hash(integer_tuple))
