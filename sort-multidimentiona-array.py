#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x:x[k])
    for i in range(n):
        print(*arr[i],sep=" ")