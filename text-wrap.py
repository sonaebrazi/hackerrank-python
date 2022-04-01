# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap

def wrap(string, max_width):
    if(max_width > len(string)):
        return False
    else:
       ls= textwrap.wrap(string,max_width)

    listToStr = '\n'.join(ls)
    return listToStr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

