'''
Intersection of two arrays:
o Question: Find the intersection of two arrays common elements in the second array.
o Sample Input: [1,2,2,1] and [2,2]
expected output: [2]
'''
arr1=[1,2,3,4,5]
arr2=[3,4,5]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i],end=" ")