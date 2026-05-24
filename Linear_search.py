def linear_search(n,arr,target):
    flag = "false"
    for i in range(n):
        if target!=arr[i]:
            pass
        else:
            loc = i
            flag ="True"
    if flag =="True":
        print("Congrasulation the target element is found at index ",loc)
    else:
        print("Sorry element not found")
    return n,arr,target


if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr = []
    for i in range(n):
        arr.append(int(input('Enter values: ')))
    target = int(input('Enter no which is to be search: '))
    linear_search(n,arr,target)