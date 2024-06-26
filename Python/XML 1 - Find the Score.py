# Name : XML 1 - Find the Score
# Link : https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
# Difficulty : Easy
# Programming language : Python

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    if len(node) == 0:
        return len(node.attrib)
    ans = 0
    for child in node:
        ans += get_attr_number(child)
    return ans+len(node.attrib)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
