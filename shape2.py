class Circle:

    def __init__(self, x):
        self.x=x

    def area(self):
        area=(self.x)*(self.x)*3.1415
        return area

    def circumference(self):
        circumference=2*3.1415*(self.x)
        return circumference

x=input("Radius:")
x=Circle(x)
print 'area:',x.area()
print 'circumference:',x.circumference()
