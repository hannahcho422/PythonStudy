# Hamburger shop

def print_menu():
    print("1. Cheeseburger Set")
    print("2. Beefburger Set")
    print("3. Chickenburger Set")
    print("4. Exit")
    
def check_menu(n):
    if 1 <= n <= 4:
        print("Menu ", n, "selected")
    else:
        print("Wrong input")
    
print_menu()

menu = int(input("Choose menu: "))

check_menu(menu)
