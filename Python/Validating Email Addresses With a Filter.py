# Name : Validating Email Addresses With a Filter
# Link : https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Difficulty : Medium
# Programming language : Python

import re


def fun(s):
    x = re.search(
        "(^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]([a-zA-Z0-9-.])?([a-zA-Z0-9-.])?$)", s)
    if x:
        return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
