class parent:
    def __init__(self):
        self.speed=100
        print("cash,Gold")

    def bike(self):
        print("splender",self.speed)

class Child(parent):
    def __init__(self):
        self.speed=150

    def bike(self):
        print("Apache",self.speed)
main------------------------------------
obj.Child()
obj.bike()
   