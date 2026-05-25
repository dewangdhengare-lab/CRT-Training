class A:
    def showA(self):
        print("I am in Class")
class B(A):
    def showB(self):
        print("I am in class B")
if __name__=="__main__":
    obj=B()
    obj.showA()
    obj.showB()

class AB:
    def showA(self):
        print("I am in Class AB")
class BC(AB):
    def showB(self):
        print("I am in class Bc")
class CA(BC):
    def showC(self):
        print("I am in class CA")
if __name__=="__main__":
    CA=CA()
    CA.showA()
    CA.showB()
    CA.showC()


class ABB:
    def showABB(self):
        print("I am in class ABB")
class BCC:
    def showBCC(self):
        print("I am in class BCC")


def add(d):
    print(d)
def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
# add(11)
# add(22,33)
add(11,22,33)