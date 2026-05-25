import re
str=input("enter any string: ")
m= re.fullmatch(str,"abcabcabc")
if m!=None:
    print("Yes matching is available at beg")
else:
    print("matching is not available at beg")