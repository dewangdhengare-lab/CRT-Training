#Sum of Five digit number
Number = int(input('Enter number'))
n1 = Number%10
Number = Number//10
n2 = Number%10
Number = Number//10
n3 = Number%10
Number = Number//10
n4 = Number%10
Number = Number//10
n5 = Number%10

result= n1+n2+n3+n4+n5
result
