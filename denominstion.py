amount = int(input("please enter amount for withdraw : "))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("notes of 100 rupee ", note1)
print("notes of 50 rupee" , note2)
print("note of rupee " , note3)