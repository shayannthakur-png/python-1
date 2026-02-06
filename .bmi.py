weight = float(input("enter weight here:"))
height = float(input("enter your height here: "))

BMI = weight / (height/100)**2
print("your bmi is ", BMI)

if BMI <= 18.4 :
    print("your underwieght")
elif BMI <= 24.9 :
    print("your healthy")
elif BMI <= 29.9 :
    print(" your overwieght")
elif BMI <= 34.9 :
    print( " your every over wieght")
elif BMI <= 39.9 :
    print(" your are obese")
else:
    print("your very obese")