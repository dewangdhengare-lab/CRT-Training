#Remove Duplicates from unsorted array:
# Question : write a function to remove duplicate from an unsorted array.
# simple input: [3,2,3,1,2,4]
# expected : [3,2,1,4]
arr=[3,2,3,1,2,4]
ans=[]
for x in arr:
    if x not in ans:
        ans.append(x)
print(ans)