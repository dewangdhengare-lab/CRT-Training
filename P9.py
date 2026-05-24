'''
check for anagrams:
o Question: Write a program to check if two string are anagrams of each other.
o Logic: Check if the character counts in both strings are the same.
o sample Input: "listen" and "silent"
o Expected output: Anagrams
'''
s1="listen"
s2="silent"
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagram")