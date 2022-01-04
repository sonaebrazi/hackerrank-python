# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
input_str = input()
l = len(input_str)
uper_list = []
lower_list = []
odd_digits = []
even_digits = []
for i in range(0,l):
    if(input_str[i].isupper()):
        uper_list.append(input_str[i])
    if (input_str[i].islower()):
        lower_list.append(input_str[i])
    if(input_str[i].isdigit()):
        n=int(input_str[i])
        if((n%2)==0):
            even_digits.append(input_str[i])
        else:
            odd_digits.append(input_str[i])
uper_list.sort()
lower_list.sort()
odd_digits.sort(key=int)
even_digits.sort(key=int)
s1=''.join(uper_list)
s2=''.join(lower_list)
s3=''.join(odd_digits)
s4=''.join(even_digits)
final=s2+s1+s3+s4
print(final)



