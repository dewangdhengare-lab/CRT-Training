import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.Capacity = 100

    def isFull(self):
        if self.top == self.Capacity - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            print(ele, "is popped")

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stack[self.top])


if __name__ == "__main__":
    obj = Stack()
    a = [234456, 122, 2, 233]

    for i in range(len(a)):
        obj.push(a[i])

    for i in range(len(a)):
        obj.pop()

    while True:
        print("1.push")
        print("2.pop")
        print("3.peek")
        print("4.traverse")
        print("0.exit")

        ch = int(input("select any choice : "))

        if ch == 1:
            ele = int(input("enter data: "))
            obj.push(ele)

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)