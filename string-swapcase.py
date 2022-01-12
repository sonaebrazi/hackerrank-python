# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(string):
    new_str = ""
    for i in range(0, len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                new_str = new_str+(string[i].lower())
            if string[i].islower():
                new_str = new_str+(string[i].upper())
        else:
            new_str=new_str+string[i]
    return new_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
