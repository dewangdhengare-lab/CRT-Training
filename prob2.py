# #input
# n=7 price[]=[100,80,60,70,60,75,85]
# output:1 1 1 8 1 8 8
# 80<100 print 1
# 60<80 print 1
# 70>60 print 2
# 60<70 print 1  
# 75>60 print 2
# 85>75 print 2
# ans**3

price=[100,80,60,70,60,75,85]
n=len(price)
res=[]
for i in range(n):
    count=1
    for j in range(i-1,-1,-1):
        if price[i]>price[j]:
            res.append(price)
            break
