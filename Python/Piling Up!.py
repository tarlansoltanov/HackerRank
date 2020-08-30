# Name : Piling Up!
# Link : https://www.hackerrank.com/challenges/piling-up/problem
# Difficulty : Medium
# Programming language : Python

from collections import deque


def check(arr):
    ans = 0
    if sum(arr)//len(arr) == arr[0]:
        return "Yes"
    while len(arr) != 0:
        if arr[len(arr)-1] > arr[0]:
            if ans == 0 or arr[len(arr)-1] <= ans:
                ans = arr.pop()
            else:
                return "No"
        elif arr[len(arr)-1] < arr[0]:
            if ans == 0 or arr[0] <= ans:
                ans = arr.popleft()
            else:
                return "No"
        else:
            if ans == 0 or arr[0] <= ans:
                ans = arr.pop()
                if len(arr):
                    arr.popleft()
            else:
                return "No"
    return "Yes"


for _ in range(int(input())):
    n = int(input())

    arr = deque(list(map(int, input().split())))

    print(check(arr))s
