import sys
class getNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class Doublelinked:
    def __init__(self):
        self.head = None

    def append(self):
        data=int(input("enter the data : "))
        newnode=getNode()
        newnode.data=data
        if self.head ==None:
            self.head=newnode
        else:
            ptr=self.head
            while ptr.right != None:
                ptr=ptr.right
            ptr.right=newnode
            newnode.left=ptr
            print(data,"is added")

    def traverse(self):
        if self.head == None:
            print("List is empty")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data,"->",end="")
                ptr=ptr.right

    def addAtbeginning(self):
        data=int(input("enter the data : "))
        newnode=getNode()
        newnode.data=data
        if self.head ==None:
           self.head=newnode
        else:
            ptr=self.head
            newnode.right=ptr
            ptr.left=newnode

            print(data,"is added")

    def addAtbetween(self):
        data=int(input("enter the data : "))
        key=int(input("enter data after inserted: "))
        newnode=getNode()
        newnode.data=data
        if self.head ==None:
            self.head=newnode
        else:
            ptr=self.head
            while ptr.right is None:
                if key == ptr.data:
                    break
                else:
                    ptr=ptr.right


            if ptr.right==None:
                print("Key Not found")
            else: 
                ptr1=ptr.right
                ptr.right=newnode
                newnode.right=ptr1
            print(key,"is added")

           

if __name__=='__main__':
        
    obj=Doublelinked()
    
    
    while True:
        print("\n1.Append")
        print("2.Traverse")
        print("3.Add at beginning")
        print("4.Add at between")
        print("0.exit")
        n=int(input("enter your choice : "))
        if n==1:
            obj.append()
        elif n==2 :
            obj.traverse()
        elif n==3:
            obj.addAtbeginning()
        elif n==4:
            obj.addAtbetween()
        elif n==0:
            sys.exit()