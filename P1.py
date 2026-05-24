#A function is a self contain block which is design and executed seperately that returns output in main funtion.
# def add(a,b):
#     # a=int(input("Enter a: "))
    # b=int(input("Enter b: "))
    # res = a+b
    # print("Addition is:",res)

# if __name__ == '__main__':
#     add()

# Function with Parameter
# if __name__ == '__main__':
#     a = int(input("Enter a: "))
#     b= int(input("Enter b: "))
#     add(a,b)

# def add(a, b):
#     res = a+b
#     return res
# #Function with return value and  parameter
# if __name__ == '__main__':
#             a = int(input("Enter a: "))
#             b= int(input("Enter b: "))
#             r = add(a,b)
#             print("Addition is:", r)

#Function with parameter and multiple return values
def add(a,b):
    res1=a+b
    res2=a-b
    res3=a*b
    return res1, res2, res3

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    r1,r2,r3 = add(a, b)
    print("Addition is:", r1)
    print("Addition is:", r2)
    print("Addition is:", r3)