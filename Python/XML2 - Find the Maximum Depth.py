# Name : XML2 - Find the Maximum Depth
# Link : https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
# Difficulty : Easy
# Programming language : Python

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    if len(elem) == 0:
        return 0
    maxx = 0
    for child in elem:
        maxx = max(maxx, depth(child, level-1))
    maxdepth = 1 + maxx
    return maxdepth


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
