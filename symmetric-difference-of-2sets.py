#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
n1=int(input())
m = set(list(map(int, input().split())))
n2=int(input())
n= set(list(map(int, input().split())))
munion=m.union(n)
mintersctn=m.intersection(n)
res=munion.difference(mintersctn)
res_lis=list(res)
res_lis.sort()
l=len(res_lis)
for i in range(l):
    print(res_lis[i])