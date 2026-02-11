print("enter marks here")
maths = int(input("enter maths marks here :"))
english = int(input("enter english marks here :"))
science = int(input("enter science marks here :"))
geography = int(input("enter geography marks here:"))
music = int(input("enter music marks here:"))
total = maths+english+science+geography+music
average = total/5

if average>=85 and average<=100:
    print("you got an A")
elif average>=65 and average<=84:
    print("you got a B")
elif average>= 45 and average<=64:
    print("you got a C")
elif average>=25 and average <=44:
    print("you got a D")
else :
    print("you got an E this means you failed")