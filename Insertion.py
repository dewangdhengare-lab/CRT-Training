def Insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        pos = i
        current = arr[i]
        while current < arr[pos-1] and pos > 0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current

if __name__=='__main__':
    arr = [6,23,2,4,1,8,56,3]
    Insertion_sort(arr)
    print(*arr)


def Insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        pos = i
        current = arr[i]
        while current > arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = current


if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    Insertion_sort(arr)
    print(*arr)
