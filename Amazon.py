# #Amazon
# give two string s and t return the minimum number of operation required to convert s to t
s='ycce'
t='ycsce'
count=0
output=0

if len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1


if len(s)<len(t):
    for i in  range(len(s)):
        if s[i]!=t[i]:
            count+=(len(t)-len(s))


if len(s)>len(t):
    for i in  range(len(s)):
        if s[i]!=t[i]:
            count+=(len(s)-len(t))
        
output==count
print(output)
    