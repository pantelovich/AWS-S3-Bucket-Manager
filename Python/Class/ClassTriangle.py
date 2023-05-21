class Triangle:
    def __init__(self, base, height, a, b, c):
        self.base = base
        self.height = height
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return (self.base * self.height) /2
    def __str__(self):
        return "Triangle - base {}, height {}".format(self.base , self.height)
    def perimeter(self):
        return self.a + self.b + self.c
triangle1 = Triangle(4,5,3,4,5)
print(triangle1)
print("The first triangles are is: ", triangle1.area())
print("The first triangles perimeter is: ", triangle1.perimeter())
