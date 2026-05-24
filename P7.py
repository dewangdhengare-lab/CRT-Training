#Reverse the number
Number = int(input('Enter the Number :'))
rev = 0
while Number>0:
    rem = Number%10
    rev = rev * 10 + rem
    Number = Number//10

print(rev)