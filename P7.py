#important program s
#-----------------------

s="Learning python is very easy from ashish sir"
l=s.split(" ")
l=[i[::-1]for i in l]
l=" ".join(l)
print(l)



I ="ABCDABBCDABBBCCCDDEEEF"
emp = ""
for i in range(len(I)):
    if I[i] not in emp:
        emp = emp + I[i]
print(emp)