#Nested list
Problem =1
arr=[11,22,33]
print(arr)
for i in range(len(arr)):
    print(arr[i])

arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
for x in range(len(arr)):
    print(arr)

#printing in Matrix format
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()


#first loop is for rows and
# second loop is for colns in matrix