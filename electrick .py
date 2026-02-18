uni = int(input("Please enter Number of Units you Consumed: "))

if uni < 50:
    amount = uni * 2.60
    surcharge = 25

elif uni <= 100:
    amount = 130 + ((uni - 50) * 3.25)
    surcharge = 35
