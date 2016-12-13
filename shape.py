class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return (self.r**2)*3.14

    def perimeter(self):
        return 2*self.r*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.r, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return (2* self.x) + (2 * self.y)

    def __str__(self):
        return "Rectangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x

class Triangle():
  def __init__(self, x, y):
    self.x=x
    self.y=y

  def area(self):
    return self.x*self.y*0.5

  def perimeter(self):
    hypotenuse=((self.x**2)+(self.y**2))**0.5
    return hypotenuse+self.x+self.y

  def __str__(self):
    return "Triangle has dimensions of x= %.2f and y= %.2f, and area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Iscoceles(Triangle):
    def __init__(self, x):
        self.x = x
        self.y = x

class Depth():
    def __init__(self, z):
        self.z=z
    def volume(self):
        return self.area()*self.z
    def surfacearea(self):
        return 2*self.area()+(self.z*self.perimeter())

class Box(Rectangle, Depth):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

class Cylinder(Circle, Depth):
    def __init__(self, r):
        self.r=r

z=Box(3,4,5)
print z.surfacearea()

cyl=Cylinder(5)
print cyl.surfacearea()

#x = Rectangle(3,4)
#print x
#y = Square(5)
#print y
