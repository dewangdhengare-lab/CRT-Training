#Find the Maximum Element:
# Question: write a function to find the maximum and minimum
# elements in an array.
# Sample input: [5,3,9,2,8]
# Expected Output: maximum: 9, Minimum: 2


arr=[5,3,9,2,8]
max=arr[0]
min=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]
    if min>arr[i]:
        min=arr[i]
print(max)
print(min)

