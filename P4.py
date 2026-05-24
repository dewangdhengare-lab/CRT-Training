'''
Array Rotation:
o Question:Rotate an array to the right by a given number of steps.
o Sample Input: [1,2,3,4,5] rotated by 2 steps
o Expected Output: [4,5,1,2,3]

ex: arr[1,2,3,4,5] k= 2 ==> [4,5,1,2,3]
'''
arr=[1,2,3,4,5]
temp = arr[-1]
k=2
for i in range(k):
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
print(arr)
    