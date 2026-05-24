import sys

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


if __name__ == "__main__":
    obj = Queue()

    while True:
        print("1.push")
        print("2.pop")
        print("3.peek")
        print("4.traverse")
        print("0.exit")

        ch = int(input("select any choice : "))

        if ch == 1:
            ele = int(input("enter data: "))
            obj.insert(ele)

        elif ch == 2:
            obj.delete()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)