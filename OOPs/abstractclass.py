from abc import ABC,abstractmethod
class Car():
    def show(self):
        print("every car has 4 wheels")

    @abstractmethod
    def speed(self):
        pass

class Maruti(Car):
    def speed(self):
        print("spedd is 100km/h")
              
class Marcedes(Car):
    def speed(self):
        print("spedd is 100km/h")

m = Maruti()
m1 = Marcedes()

m.show()
m.speed()
m1.show()
m1.speed()