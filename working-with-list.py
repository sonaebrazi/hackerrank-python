if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=set(arr)
    arr2=list(arr1)
    arr2.sort()
    l=len(arr2)
    print(arr2[l-2])