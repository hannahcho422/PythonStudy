integer = int(input("Enter an integer: "))

i = 1
product = 1

while i <= integer :
    product = product * i
    i += 1

print(integer, "! = ", product)