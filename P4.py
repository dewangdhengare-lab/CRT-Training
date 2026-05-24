#Tech Number
#A number is called a tech number if the given number has an even number of digits and the number can be divided
# exactly into two parts from the middle. After equally dividing the number,Sum up the numbers and find the squareof the sum.
# if we get the number itself ar square


Number=int(input("Enter tech number: "))
Save = Number
count=0
while Number>0:
    Number = Number//10
    count = count + 1
Number =Save
if count%2==0:
    mid = count//2
    n1 = Number%10**mid
    # Number = Number//10
    n2 = Number //10**mid

    result = (n1+n2)**2
    if result == Save:
        print("Number is Tech Number.",result)
    else:
        print("Number is not a tech Number.",result)