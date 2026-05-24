from xml.dom.minidom import ProcessingInstruction


P =(input("Enter phone number: "))
# if len(P) == 10 and P.isdigit()==True and P.statwith(("5","6","7","8","9")):
#     print("Valid")
# else:
#     print("Not valid")
if P.isdigit():
    if len(P)==10:
        if P.startswith(9) or P.startswith(7):
            print("Valid")
        else:
            print("Not Valid")
    else:
        print("Please enter 10 digits only")
else:
    print("Please enter no is digit format ")