#delete element from any location
arr=[]
n = int(input("Enter size :"))
for i in range(n):
    arr.append(int(input("Enter no: ")))
key = int(input("Enter key element which is to be inserted :"))
arr.append(0)
for i in range(len(arr)-2):
    if key == arr:
        arr[key].pop
print(arr)
