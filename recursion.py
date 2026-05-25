def fact(n):
    if n ==1 and n ==0:
        return
    else:
        return n*fact(n-1)

if __name__=='__main__':
    n=5
    res = fact(n)