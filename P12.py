#check number is armstrong
number = int(input('Enter the  number'))
sum = 0
save = number

Count = 0
while number>0:
    Count = number//10
    Count = Count + 1
    number = save

while number>0:
    rem = number%10
    sum = sum+(rem**Count)
    number = number//10

if sum==save:
    print("number is arstrong")
else:
    print("number is not armstrong")