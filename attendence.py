med = input("did you have a medical note YES/NO: ").strip().upper()

if med =='y' :
    print("you are allowed")

atten = int(input("Enter the attendance of the student: "))

if atten >= 75:
    print("Allowed")
else:
    print("Not allowed")
