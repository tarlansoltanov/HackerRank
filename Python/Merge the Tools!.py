# Name : Merge the Tools!
# Link : https://www.hackerrank.com/challenges/merge-the-tools/problem
# Difficulty : Medium
# Programming language : Python

def merge_the_tools(string, k):
    ans = []
    st = 0

    for part in zip(*[iter(string)]*k):
        m = []
        for i in part:
            if i not in m:
                m.append(i)
        print(''.join(m))
