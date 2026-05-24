def Selction_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m =arr[i]
        for j in range(i+1,n):
            if m > arr[j]:
                m = arr[j]
                loc = j
                arr[i],arr[loc]=arr[loc],arr[i]



if __name__=='__main__':
    arr = [6,23,2,4,1,8,56,3]
    Selction_sort(arr)
    print(*arr)

def Selction_sort(arr):
    n = len(arr)
    for i in range(n):
        m =arr[i]
        for j in range(n):
            if m > arr[j]:
                m = arr[j]
                loc = j
                arr[i],arr[loc]=arr[loc],arr[i]



if __name__=='__main__':
    arr = [6,23,2,4,1,8,56,3]
    Selction_sort(arr)
    print(*arr)
