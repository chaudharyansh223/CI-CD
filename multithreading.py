from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("ansh")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("DevOps")
            sleep(1)

t1 = A()
t2 = B()

t1.start()#we use start() instead of run() bcz only when imported Thread will work
t2.start()

t1.join()#join mtlb phle t1 and t2 apne kaam karengi then phir print() execute hoga
t2.join()

print("om namaha shivay")#aisa karne se ye print() t1 and t2 ko disturb karra agar aise na disturb karre toh uske lia
