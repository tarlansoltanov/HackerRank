# Name : Nested Lists
# Link : https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty : Easy
# Programming language : Python

if __name__ == '__main__':
    arr = []
    nums = []
    for _ in range(int(input())):
        name = input()
        arr.append(name)
        score = float(input())
        arr.append(score)
        nums.append(score)
    nums = set(nums)
    nums.remove(min(nums))
    ans = [arr[a-1] for a in range(0, len(arr)) if arr[a] == min(nums)]
    ans = list(ans)
    ans.sort()
    for i in range(0, len(ans)):
        print(ans[i])
