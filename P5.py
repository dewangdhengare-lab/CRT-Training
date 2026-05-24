#Reverse of three digit number

Number = int(input('Enter number'))
n1 = Number%10
Number = Number//10
n2 = Number%10
Number = Number//10
n3 = Number%10

result= n1*100+n2*10+n3*1
result
