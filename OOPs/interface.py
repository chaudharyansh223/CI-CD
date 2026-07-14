from abc import ABC,abstractmethod
class Shape():
    @abstractmethod
    def show(self):
        pass

class Square(Shape):
    def show(self):
        print("square has 4 sides")

class Circle(Shape):
    def show(self):
        print("circle has round shape")

sq1 = Square()
cr1 = Circle()

sq1.show()
cr1.show()
