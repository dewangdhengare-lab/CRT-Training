#Take input from user and print / insert it into list
#a,b,c=map(int,input().split())
#arr= map(int,input().split())
#Sum of list elements
n = int(input("Enter number of items :"))
print("Enter list element: ")
arr=[]
sum = 0
even=0
odd=0
etot=0
otot=0
for i in range(n):
    ele=int(input("Enter element:"))
    arr.append(ele)
for i in range(len(arr)):
    print(arr[i],end=" ")
    #Sum
    sum = sum + arr[i]
    if arr[i]%2==0:
        even = even + 1
        #sum of even numbers in list
        etot= etot +arr[i]

    else:
        odd = odd +1
        #sum of odd numbers in list
        otot = otot + arr[i]


print("\nThe sum if list",sum)
print("Even :", even)
print("Odd", odd)
print("Even Total: ",etot)
print("Odd Total: ",otot)
