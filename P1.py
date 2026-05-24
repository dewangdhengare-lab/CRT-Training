# Reverse queue using stack
import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.Capacity = 5

    def isfull(self):
        if self.top == self.Capacity - 1:
            return True
        else:
            return False

    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isfull():
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            print(ele, "is popped")

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(self.stack[self.top])

class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.Capacity = 5

    def isfull(self):
        if self.rear == self.Capacity - 1:
            return True
        else:
            return False

    def isempty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def insert(self, ele):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.queue.append(ele)
            print(ele, "is pushed")

    def delete(self):
        if self.isempty():
            print("Queue is empty")
        else:
            ele = self.queue[self.front]
            for i in range(1,self.rear+1):
                self.queue[i-1] = self.queue[i]
                self.rear-=1
            return print(ele)
            # ele = self.queue.pop[0]
            # self.front = self.front - 1
            # print(ele, "is popped")

    def traverse(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i],end=" ")

    def peek(self):
        pass
        if self.isempty():
            print()
        else:
            print(self.queue[self.rear])

if __name__=='__main__':
    obj1 = Queue()
    obj2 = Stack()
    for i in range(obj1.Capacity):
        ele = int(input("Enter element :"))
        obj1.insert(ele)

    for i in range(obj1.Capacity):
        ele = obj1.delete
        obj2.push(ele)

    for 