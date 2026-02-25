# Program to check if a student can enroll in Raj's class

age = int(input("Enter the student's age: "))

if age >= 10 and age <= 20:
    print("Student is eligible to enroll in the class.")
elif age > 20:
    print("Student is NOT allowed to enroll (age is above 20).")
else:
    print("Student is NOT allowed to enroll (age is below 10).")