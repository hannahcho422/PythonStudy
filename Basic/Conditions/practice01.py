price = int(input("Enter product price: "))

if price >= 100000 :
    discount = price * 0.05
    sales = price - discount
    
print("Total price: ", sales)