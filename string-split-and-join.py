# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
def split_and_join(line):
    # write your code here
    new_str = ""
    line_arr = line.split()
    new_str = "-".join(line_arr)
    return new_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)