#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
def average(array):
    num_list=list(set(array))
    l=len(num_list)
    sum=0
    for i in range(l):
        sum=sum+num_list[i]
    avg=round((sum/l),3)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)