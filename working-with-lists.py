# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    list = []
    N = int(input())
    for i in range(N):
        full_command = input()
        splited = full_command.split()
        command = str(splited[0])

        if command == "print":
            print(list)
        if command == "insert":
            list.insert(int(splited[1]), int(splited[2]))
        if command == "append":
            list.append(int(splited[1]))
        if command == "sort":
            list.sort()
        if command == "pop":
            list.pop()
        if command == "reverse":
            list.reverse()
        if command == "remove":
            list.remove(int(splited[1]))
