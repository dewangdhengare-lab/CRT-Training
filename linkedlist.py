import sys
class getNode:
    def __init__(self):
        self.data=None
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def append(self):
        data=int(input("Enter data: "))
        newNode=getNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(data,"is added")

    def traverse(self):
        if self.head==None:
                print("Linked list not present")
        else:
                ptr=self.head
                while ptr!=None:
                    print(ptr.data,'->',end="")
                    ptr=ptr.next
    def addBegin(self):
        data = int(input("Enter data: "))
        newNode = getNode()
        newNode.data = data
        if self.head == None:
            self.head = newNode
        else:
            ptr = self.head
            newNode.next=ptr
            self.head=newNode
        #     newNode.next = self.head
        #     self.head = newNode
        #     print(data,"is added\n")
        # print()
    def addBetween(self):
        data = int(input("Enter data: "))
        key = int(input("Enter data after inserted: "))
        newNode = getNode()
        newNode.data = data
        if self.head == None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next!=None:
                if key == ptr.data:
                    break
                else:
                    ptr=ptr.next
            if ptr.next==None:
                print("Next not found.")
            else:
                ptr1 = ptr.next
                ptr.next = newNode
                newNode.next=ptr1
                print(data," is added")

    def deleteAtBegin(self):
        if self.head==None:
            print("List not present")
        else:
            ptr=self.head
            ptr1=ptr.next
            ptr.next=None
            self.head=ptr1
            print(ptr.data,"is deleted.")

    def deleteAtEnd(self):
        if self.head==None:
            print("List not present.")
        else:
            ptr = self.head
            while ptr.next!=None:
                ptr1=ptr
                ptr=ptr.next
            ptr.next=None
            print(ptr.data,"is deleted")
    def length(self):
        count = 0
        if self.head==None:
            print("List not present")
        else:
            ptr = self.head
            while ptr !=None:
                count = count + 1
                ptr = ptr.next
        print("Length of linkedlist :",count)

if __name__=='__main__':
    obj = linkedlist()
    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Begin")
        print("4. AddBetween")
        print("5. DeleteAtEnd")
        print("6. Length of linkedlist")
        print("0. Exit")
        n=int(input("Select any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addBegin()
        elif n==4:
            obj.addBetween()
        elif n==5:
            obj.deleteAtBegin()
        elif n==6:
            obj.length()
        elif n==0:
            sys.exit(0)