from shapes import circle,rectangle

r=int(input("Enter radius of circle: "))
b=int(input("Enter breadth of rectangle: "))
l=int(input("Enter length of rectangle: "))

print("Area of the circle : ",circle.area(r))
print("Perimeter of the circle : ",circle.perimeter(r))

print("Area of the rectangle : ",rectangle.area(l,b))
print("Perimeter of the rectangle : ",rectangle.perimeter(l,b))