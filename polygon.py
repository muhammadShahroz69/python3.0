print("POLYGON AREA CALCULATOR")
print("-----------------------")

def triangle_area():
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle is:", area)


def rectangle_area():
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    area = length * breadth
    print("Area of Rectangle is:", area)


def square_area():
    side = float(input("Enter side of square: "))
    area = side * side
    print("Area of Square is:", area)


def circle_area():
    radius = float(input("Enter radius of circle: "))
    area = 3.14 * radius * radius
    print("Area of Circle is:", area)


print("\nChoose a polygon:")
print("1. Triangle")
print("2. Rectangle")
print("3. Square")
print("4. Circle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    triangle_area()
elif choice == 2:
    rectangle_area()
elif choice == 3:
    square_area()
elif choice == 4:
    circle_area()
else:
    print("Invalid choice")