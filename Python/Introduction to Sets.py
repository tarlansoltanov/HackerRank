# Name : Introduction to Sets
# Link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty : Easy
# Programming language : Python

def average(array):
    ans = sum(set(array))/len(set(array))
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
