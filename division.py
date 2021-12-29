#https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
c=a//b
d=a-b*c
answer_tuple=(c,d)
print(answer_tuple)