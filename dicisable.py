print("enter a number (numarator)")
numm = int(input())
print("enter dinomerator here")
numd = int(input())

if numd%numm==0:
 print("\n"+str(numm)+ " is divisable by "  +str(numd))
else:
  print("\n"+str(numm)+" is not divisable by " +str(numd))