import sys

class Binary_Search:
    def __init__(self,key):
        self.leftChild = None
        self.data = key
        self.rightChild = None
    def insert(self,key):
            if self.data==None:
                self.data=key
                return
            elif self.data==key:
                return
            else:
                if key<self.data:
                    if self.leftChild:
                        self.leftChild.insert(key)
                    else:
                        self.leftChild=Binary_Search(key)
                elif key>self.data:
                    if self.rightChild:
                        self.rightChild.insert(key)
                    else:
                        self.rightChild=Binary_Search(key)
    def preorder(self):
            print(self.data,end="->")
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    def postorder(self):
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(self.data, end="->")
    def inorder(self):
            if self.leftChild:
                self.leftChild.inorder()
            print(self.data, end="->")
            if self.rightChild:
                self.rightChild.inorder()
    def search(self,key):
        if self.data == key:
            print("key is found")
        else:
            print("key not found")
            return
        if key < self.data:
            if self.leftChild:
                self.leftChild.search(key)
            else:
                self.leftChild = Binary_Search(key)
        elif key > self.data:
            if self.rightChild:
                self.rightChild.search(key)
            else:
                self.rightChild = Binary_Search(key)



if __name__=='__main__':
    root = Binary_Search(None)
    while True:
        print("1. Insert")
        print("2. Preorder")
        print("3. Postorder")
        print("4, Inorder")
        print("5. search")
        print("0. Exit")
        n = int(input("Select your"
                      " choice: "))
        if n==1:
            arr=[36,26,46,21,31,11,24,41,56,51,66]
            for i in range(len(arr)):
                root.insert(arr[i])
        elif n==2:
            root.preorder()
        elif n==3:
            root.postorder()
        elif n==4:
            root.inorder()
        elif n==5:
            n =int(input("Enter key: "))
            root.search(n)
        elif n==0:
            sys.exit(0)