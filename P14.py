number = int(input('Enter the number'))
fact = 1
rem = 0
while number > 0:
        rem = number%10
        print(rem)
        fact=1
        while rem>0:
            fact = fact * rem
            rem = rem-1
            number = number//10
print(number)
