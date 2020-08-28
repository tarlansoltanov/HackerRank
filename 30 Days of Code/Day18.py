# Name : Day 18: Queues and Stacks
# Link : https://www.hackerrank.com/challenges/30-queues-stacks/problem
# Difficulty : Easy
# Programming Language : Python

import sys

from collections import deque


class Solution:
    stack = []
    queue = deque()

    def pushCharacter(self, s):
        self.stack.append(s)

    def enqueueCharacter(self, s):
        self.queue.append(s)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()


s = input()

obj = Solution()

l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
