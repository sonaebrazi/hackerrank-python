#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    leap = False
    # Write your logic here
    y=year
    if((y%400==0) or
    (y%100!=0) and
    (y%4)==0):
        leap=True
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))