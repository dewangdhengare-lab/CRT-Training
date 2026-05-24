'''
Check for a valid palindromic String:
o Question: Write a program to check if a given String is a valid Palindromic string after ignoring non-alphanumeric
character and considering case.
o Logic: Use loops to compare characters while ignoring non-alphanumeric characters.
o Sample Input: "A man, a plan, a canal: Panama"
o Expected output: Valid Palindrome
'''
Char="A man, a plan, a canal: Panama"
str=""
# for i in range(len(Char)):
#     if Char[i].isalpha():
#         str = Char[i] +str
#     for x in range()
# print(str.lower())
# for i in range(len(Char)):
#     for j in range(len(str)):
#         if Char[i] == str[j]:
#             print("Palindrome")
for i in range(len(Char)):
    if Char[i].isalpha():
        str += Char[i].upper()
print(str)

rev=""
for i in range(len(str)-1,-1,-1):
    rev+=str[i]
if str==rev:
    print("string is palindrome")
else:
    print("Not palindrome")