# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re


def count_substring(string, sub_string):
    count = 0
    for pos in range(len(string)):
        if string[pos:].startswith(sub_string):
            count += 1
    return count


string = input()
sub_string = input()
l = len(sub_string) - 1
c = count_substring(string, sub_string)
indx=[]
if(c!=0):
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            indx.append(i)
    for i in range(0,c):
        t=(indx[i],indx[i]+l)
        print(t)
if(c==0):
    t=(-1,-1)
    print(t)