price = int(input("Enter product price: "))
bill_1000 = int(input("Enter number of 1000won bills: "))
coin_500 = int(input("Enter number of 500won coins: "))
coin_100 = int(input("Enter number of 100won coins: "))

change = 1000 * bill_1000 + 500 * coin_500 + 100 * coin_100 - price

change_500 = change // 500
change = change % 500

change_100 = change // 100
change = change % 100

change_10 = change // 10
change = change % 10

change_1 = change

print("Change: 500won = ", change_500, ", 100won = ", change_100, ", 10won = ",change_10, ", 1won = ", change_1)

