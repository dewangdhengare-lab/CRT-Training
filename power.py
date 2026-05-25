def power(x,y):
        if y == 1:
            return x
        elif x == 1:
            return y
        elif x == 0 or y == 0:
            return 0
        else:
            return 2*power(x, y - 1)

if __name__ == '__main__':
        print(power(2,5))