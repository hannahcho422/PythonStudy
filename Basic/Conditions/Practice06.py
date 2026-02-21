apple_quality = input("Enter the quality of apples: ")

if (apple_quality == "fresh"):
    apple_price = int(input("Enter the price of an apple: "))
    if (apple_price < 1000) :
        print("Purchase 10 apples")
    else :
        print("Purchase 5 apples")
else :
    print("Don't purchase the apples")