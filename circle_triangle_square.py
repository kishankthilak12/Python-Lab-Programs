class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):

        return 3.14*(self.radius*self.radius)
    def perimeter(self):
        return 2*3.14*self.radius
    def compare(self,other):
        if self.area()>other.area():
            print("First circle has larger area")
        elif self.area()<other.area():
            print("Second circle has larger area")
        else:
            print("Both circles have equal area")

class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        return (self.side*self.side)
    def perimeter(self):
        return 4*self.side
    def compare(self,other):
        if self.area()>other.area():
            print("First square has larger area")
        elif self.area()<other.area():
            print("Second square has larger area")
        else:
            print("Both square have equal area")

class Triangle:
    def __init__(self,base,height,side1,side2):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
    def area(self):
        return 0.5*(self.base*self.height)

    def perimeter(self):
        return self.base+self.side1+self.side2

    def compare(self,other):
        if self.area()>other.area():
            print("First traingle has larger area")
        elif self.area()<other.area():
            print("Second traingle has larger area")
        else:
            print("Both traingle have equal area")

c1=Circle(5)
c2=Circle(4)
print("Area of the rectangle 1 : ",c1.area())
print("Perimeter of the rectangle 2 : ",c1.perimeter())
print("Area of the rectangle 1 : ",c2.area())
print("Perimeter of the rectangle 2 : ",c2 .perimeter())
c1.compare(c2)

s1=Square(8)
s2=Square(10)
print("\nArea of the square 1 : ",s1.area())
print("Perimeter of the square 1 : ",s1.perimeter())
print("Area of the square 2 : ",s2.area())
print("Perimeter of the square 2 : ",s2.perimeter())
s1.compare(s2)


t1=Triangle(10,8,6,7)
t2=Triangle(8,5,4,3)
print("\nArea of the triangle 1 : ",t1.area())
print("Perimeter of the triangle 1 : ",t1.perimeter())
print("Area of the triangle 2 : ",t2.area())
print("Perimeter of the triangle 2 : ",t2.perimeter())
t1.compare(t2)