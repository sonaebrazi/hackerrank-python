#https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def print_full_name(first, last):
    # Write your code here
    print("Hello %s %s! You just delved into python." %(first_name,last_name) )


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)