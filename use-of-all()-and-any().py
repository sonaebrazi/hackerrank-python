#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
def isposetive(n):
    if (n>=0):
       return True
    else:
        return False

def ispalindromic(n):
    temp = n
    rev = 0
    while (n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if (temp == rev):
        return True
    else:
        return False
n=int(input())
num_list=list(map(int,input().split()))
new_list1=list(map(isposetive,num_list))
new_list2=list(map(ispalindromic,num_list))
if(all(new_list1)):
    if(any(new_list2)):
        print(True)
    else:
        print(False)
else:
    print(False)