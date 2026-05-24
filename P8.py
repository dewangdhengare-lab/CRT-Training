#count the number of digits
Number = int(input('Enter the number'))
count = 0

while Number:
    Number = Number//10
    count = count + 1
print(count)