class triangle():
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

class iscoceles(triangle):
    def __init__(self, x):
        self.x = x
        self.y = x


x = triangle(3,4)
print x

y=iscoceles(5)
print y
