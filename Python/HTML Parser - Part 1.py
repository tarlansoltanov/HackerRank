# Name : HTML Parser - Part 1
# Link : https://www.hackerrank.com/challenges/html-parser-part-1/problem
# Difficulty : Easy
# Programming language : Python

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print(f'-> {i[0]} > {i[1]}')

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print(f'-> {i[0]} > {i[1]}')


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
