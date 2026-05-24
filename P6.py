#Accept 9 digit number and find sum of 1st and last digit (in 3 steps)
Number = int(input('Enter number'))
n1 = Number//100000000
n2 = Number%10

print(n1+n2)
# result = n1
# print(result)