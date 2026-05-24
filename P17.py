#If else and elif condition
#WAP to accept cost price from user and ask whether the user is a student or not.
#If the user is student and cost price is greater than 500, give discount of 10% ELSE discount will be 5%.
#If user is not student and cost prise is greater 500 then give discount of 8% ELASE discount wil be 2%.


#cost price:
#total discound:
#net price:
Cost_Price = int(input("Enter the cost price: "))
user_s_not = str(input("Enter S if your student else N: " ))

if user_s_not == "S":
    if Cost_Price >500:
        dis = Cost_Price*0.10
        print("You get discount of 10% on your Cost price",dis)
    else:
        dis = Cost_Price*0.05
        print("You get discount of 5% on your Cost price",dis)
elif user_s_not == "N":
    if Cost_Price >500:
        dis = Cost_Price*0.08
        print("You get discount of 8% on your Cost price",dis)
    else:
        dis = Cost_Price*0.2
        print("You get discount of 2% on your Cost price",dis)
else:
    print("No discount")


