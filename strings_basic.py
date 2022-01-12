#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from curses.ascii import isupper, isdigit, islower, isalpha, isalnum


def has_any_alphanum(s):
    arr=list(map(isalnum,s))
    if any(arr):
        return True
    else :
        return False



def has_any_alphabetic(s):
    arr=list(map(isalpha,s))
    if any(arr):
        return True
    else :
        return False


def has_any_digit(s):
    arr=list(map(isdigit,s))
    if any(arr):
        return True
    else :
        return False


def has_any_lower(s):
    arr=list(map(islower,s))
    if any(arr):
        return True
    else :
        return False

def has_any_upper(s):
    arr=list(map(isupper,s))
    if any(arr):
        return True
    else :
        return False


if __name__ == '__main__':
    s = input()
    print(has_any_alphanum(s))
    print(has_any_alphabetic(s))
    print(has_any_digit(s))
    print(has_any_lower(s))
    print(has_any_upper(s))

