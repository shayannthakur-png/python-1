base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

result = 1
i = 1

while i <= exponent:
    result = result * base
    i = i + 1

print("Answer =", result)