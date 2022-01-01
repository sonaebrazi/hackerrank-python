if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=student+[[name,score]]
    l= len(student)
    student = sorted(student, key=lambda x: x[0])
    score_list=list(map(lambda x:x[1],student))
    score_set=set(score_list)
    score_listnew=list(score_set)
    score_listnew.sort()
    for i in range (0,l):
        if(student[i][1]==score_listnew[1]):
            print(student[i][0])

