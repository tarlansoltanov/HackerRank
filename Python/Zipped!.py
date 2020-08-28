# Name : Zipped!
# Link : https://www.hackerrank.com/challenges/zipped/problem
# Difficulty : Easy
# Programming language : Python

n, m = map(int, input().split())
ans = []
for i in range(m):
    k = list(map(float, input().split()))
    ans.append(k)
ans = list(zip(*ans))

for i in range(n):
    ans1 = sum(ans[i])
    print(ans1/m)
