uni = int(input("Please enter Number of Units you Consumed: "))

if uni < 50:
    amount = uni * 2.60
    surcharge = 25

elif uni <= 100:
    amount = 130 + ((uni - 50) * 3.25)
    surcharge = 35
elif uni <= 100:
    amount = 130 + ((uni - 50) * 3.25)
    surcharge = 35

elif uni <= 200:
    amount = 130 + 162.50 + ((uni - 100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((uni - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("energy bill =",  total)
