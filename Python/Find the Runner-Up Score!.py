# Name : Find the Runner-Up Score!
# Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty : Easy
# Programming language : Python

def second_max(arr):
    arr.remove(max(arr))
    return max(arr)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    print(second_max(arr))
