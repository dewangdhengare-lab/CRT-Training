#Find the number is palindrome
Number = int(input('enter the number'))
Save = Number
rev = 0

while Number >0:
    rem = Number%10
    rev = rev*10+rem
    Number = Number//10

if rev==Save:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
