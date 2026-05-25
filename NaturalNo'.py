def naturalNo(n):
    if n == 0 or n == 1:
        return 0
    else:
        return n*(n+1)//2

if __name__ == '__main__':
        print(naturalNo(10))