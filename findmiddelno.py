Program 12: Find middle of three numbers
print("Ajay Rajput")
print("rollno 0818CL241013")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a > c and a < b):
    print(a)
elif (b > a and b < c) or (b > c and b < a):
   print(b)
else:
   print(c)