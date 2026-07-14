class A: #parent clas
    def disp(self):
        print("parent class method")

class B(A): #child clas
    def disp(self):
        super().disp()#super() used only to access parent class function as well.
        print("child class method")

c1 = B()
c1.disp() 