# Calculate Factorial

integer = int(input("Enter an integer: "))

product = 1

for i in range(1, integer + 1) :
    product = product * i

print(integer, "! = ", product)