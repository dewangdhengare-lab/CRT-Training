#   j0  j1  j2  j3      ASCII Values
#i=1 1  1   1   1      A-65 a-97    0-48
#i=2    2   2   2      B-66 b-98    1-49
#i=3    3   3   3      C-67 c-99    2-50
#i=4    4   4   4
#----------------
#i= j=1



# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end="\t")
#         n=n +1
#     print()
#
# n=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end=" ") #"chr" is used to convert Number values into Character values and "ord" is the opposite of chr
#         n=n+1
#     print()
sum = 0
for i in range(1,5):
    for j in range(1,i+1):
            sum = [i]+[j]
            print(i,end=" ")
    print()


for i in range(4,0,-1):
    for j in range(1,i+1):
        print(" ",end=" ")
    print("*")

sp=0
for i in range(4, 0, -1):
        for x in range(sp):
            print(" ",end="")
        for j in range(1, i + 1):
            print("* ", end=" ")
        print()
        sp=sp+1


