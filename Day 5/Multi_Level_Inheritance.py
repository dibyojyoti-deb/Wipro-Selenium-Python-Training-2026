class A:
    def showa(self):
        print("A")

class B(A):
    def showb(self):
        print("B")

class C(B):
    def showc(self):
        print("C")

obj=C()
obj.showa()
obj.showb()
obj.showc()