#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab=int(input())
bc=int(input())
teta_radian=math.atan(ab/bc)
teta=math.degrees(teta_radian)
teta=round(teta)
print(f"{teta}\N{DEGREE SIGN}")