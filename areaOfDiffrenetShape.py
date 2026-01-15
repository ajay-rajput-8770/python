print("Ajay Rajput")
print("rollno 0818CL241013")
print("Choose a shape to find its area:")
print("1. Circle")
print("2. Square")
print("3. Triangle")
print("4. Cube (Surface Area)")
print("5. Rectangle")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif choice == 2:
    side = float(input("Enter side of square: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 3:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

elif choice == 4:
    side = float(input("Enter side of cube: "))
    area = 6 * (side * side)
    print("Surface Area of Cube =", area)

elif choice == 5:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
    print("Area of Rectangle =", area)

else:
    print("Invalid choice! Please enter between 1 and 5.")