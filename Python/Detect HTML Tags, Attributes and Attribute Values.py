# Name : Detect HTML Tags, Attributes and Attribute Values
# Link : https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
# Difficulty : Easy
# Programming language : Python

from html.parser import HTMLParser


class Parser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for i in attr:
            print(f'-> {i[0]} > {i[1]}')


parser = Parser()

for i in range(int(input())):
    html = input()
    parser.feed(html)
