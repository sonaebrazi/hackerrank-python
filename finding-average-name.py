#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    i=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    name_list=student_marks.keys()
    query_name = input()
    if(query_name in name_list):
        lst=list(student_marks[query_name])
        l=len(lst)
        sum=0
        for i in range (0,l):
            sum=sum+lst[i]
        avg=sum/l
        print("%.2f" % avg)