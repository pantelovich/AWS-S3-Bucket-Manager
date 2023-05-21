

class shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height
    def perimeter(self):
        return (self.height *2) + (self.base *2)


class Square(shape):
    def __init__(self, length):
        super().__init__(length, length)


class Rectangle(shape):
    def __init__(self, base, height):
        super().__init__(base, height)


class Triangle(shape):
    def __init__(self, base, height, a, b, c):
        super().__init__(base, height)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.base * self.height) /2
    def perimeter(self):
        return self.a + self.b + self.c
    
listOfShapes = [Square(5), Rectangle(5,2), Triangle(5,2,3,4,5)  ]
for shape in listOfShapes:
    print("Area: ", shape.area()," Perimeter: ", shape.perimeter())


# square1 = Square(4)  
# square2 = Square(16)                                   
# # print(square1) 
# print(square1)
# print(square1.area())
# print(square1.perimeter())
# print(square2) 
# print(square2.area())
# print(square2.perimeter()) 
# print("-"*50)
# rectangle1 = rectangle(4,5)
# print("Recangular - length: {} - height: {}".format(rectangle1.base, rectangle1.height))
# print(rectangle1.area())
# print(rectangle1.perimeter())
# print("-"*50)
# triangle1 = Triangle(4,5,3,4,5)
# print(triangle1)
# print("The first triangles are is: ", triangle1.area())
# print("The first triangles perimeter is: ", triangle1.perimeter())