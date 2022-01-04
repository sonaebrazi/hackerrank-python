# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import re

N = int(input())
for i in range(N):
    try:
        result=bool(re.compile(input()))
        print(result)
    except re.error:
        print( False)
