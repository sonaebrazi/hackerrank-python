# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re

lines = ""
n = int(input())
for i in range(n):
    lines = lines + input() + "\n"

while " && " in lines:
    lines = re.sub(r"\s\&\&\s", " and ", lines)

while " || " in lines:
    lines = re.sub(r"\s\|\|\s", " or ", lines)

print(lines)
