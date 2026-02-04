cost= float(input("please enter the actual product price :" ))
sale= float(input("enter your selling price :"))

if (sale > cost):
    amount= sale- cost
    print("total profit = {0}".format(amount)) 
else:
    print("NO PROFIT SO DONT DO")

