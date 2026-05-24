#ascending order
def Bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n):
            if arr[j]>arr[j+1]: #arr[j],arr[j+1]=arr[j+1],arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

if __name__=='__main__':
    arr = [6,23,2,4,1,8,56,3]
    Bubble_sort(arr)
    print(*arr)

#decending order
def Bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n):
            if arr[j]<arr[j+1]: #arr[j],arr[j+1]=arr[j+1],arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

if __name__=='__main__':
    arr = [6,23,2,4,1,8,56,3]
    Bubble_sort(arr)
    print(*arr)