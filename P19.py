#print 1,2,3,4,5,10,9,7,6

i=1
j=10
# while i<j:
#     print(i,"\t",j)
#     i=i+1
#     j=j-1



while i<j:
    if i==3:
        i=i+1
        j=j-1
        continue
    print(i,"\t",j)
    i=i+1
    j=j-1

    #when we should use array? Answer= When we want a single variable to store multiple value in it because in normal variable we cannot initialize multiple values.
