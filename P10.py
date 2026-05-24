'''

'''

# def staircase(n):
#     for i in range(1, n+1):
#         print(" " * (n - i) + "#" * i)
#
# staircase(4)
arr = [1,3,5,7,9]
min = 0
max = 0
for i in arr:
    if arr[i] != 9:
        min = arr[i] + min
        i = i +1
    if i != 1:
        max = arr[i] + max
print(min," ", max)