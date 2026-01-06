# Program 13: Voting Eligibility with ID Check
print("Ajay Rajput")
print("rollno 0818CL241013")
age = int(input("Enter your age: "))
ID = input("Do you have valid ID (yes/no): ").lower()
if age >= 18 and ID == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")