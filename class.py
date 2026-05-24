class Student:
    def show(self):
        print("I am a students")

s=Student()
s.show()

class Student:
    def __init__(self):
        print("Default Constructor")

    def show(self):
        print("I an in show")
n=Student()
n.show()
