#implement stack using linked list
import sys
class getNode:
    def __init__(self):
        self.data = None
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        data=int(input("enter the data : "))
        newnode=getNode()
        newnode.data=data
        if self.top == None:
            self.top=newnode
        else:
            newnode.next = self.top
            self.top = newnode
        print(data,"stack pushed")


    def traverse(self):
        if self.top == None:
            print("List is empty")
        else:
            ptr=self.top
            print("stack elements:")
            while ptr != None:
                print(ptr.data)
                ptr=ptr.next
            

    def peek(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print(self.top.data,"is peeked")

 

    def pop(self):
        if self.top == None:
            print("Stack is empty")
        else:
            data = self.top.data
            self.top = self.top.next
            print(data,"is deleted")

if __name__=='__main__':
    obj=Stack()
    while True:
        print("1.Push")
        print("2.Traverse")
        print("3.Peek")
        print("4.Pop")
        print("0.Exit")
        n=int(input("enter your choice : "))
        if n==1:
            obj.push()
        elif n==2 :
            obj.traverse()
        elif n==3:
            obj.peek()
        elif n==4:
            obj.pop()
        elif n==0:
            sys.exit(0)
            ptr=ptr.next
            ptr1.next=None
            print(ptr.data,"is deleted")
            

