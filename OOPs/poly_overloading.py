class A:
    def show(self):
        print("welcome")

    def show(self, firstname=''):
        print("welocme", firstname)

    def show(self,firstname='',lastname=''):
        print("welcome",firstname,lastname)

a1 = A()
a1.show("ansh")
a2 = A()
a2.show("chaudhary", "ansh")



        
