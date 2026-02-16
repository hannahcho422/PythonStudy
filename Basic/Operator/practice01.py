apple = int(input("Enter the number of apples: "))
pear = int(input("Enter the number of pears: "))
melon = int(input("Enter the number of melons: "))

apple_toal = apple * 1000 * 0.9     # converts to float
pear_total = pear * 2000
melon_total = melon * 3000

total = apple_toal + pear_total + melon_total

total = int(total)

print("Total price: ", total)