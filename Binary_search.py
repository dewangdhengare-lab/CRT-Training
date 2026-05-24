def Binary_search(n,arr,target):
    flag = False
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            flag = True
            loc = arr[mid]
            break
        elif target <=arr(mid):
            high = mid+1
        elif target >=arr(mid):
            low = mid+1

    if flag == True:
        print("Search is successful and present at ",loc)
    else:
        print("search is unsuccessful")

if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr = []
    for i in range(n):
        arr.append(int(input('Enter values: ')))
    target = int(input('Enter no which is to be search: '))
    Binary_search(n, arr, target)