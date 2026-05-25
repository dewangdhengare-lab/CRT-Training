def fibo(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

n=10
for i in range(n):
        print(fibo(i),end=" ")