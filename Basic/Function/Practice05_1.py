# Hamburger shop

def print_menu():
    print("1. Cheeseburger Set")
    print("2. Beefburger Set")
    print("3. Chickenburger Set")
    print("4. Exit")

def check_menu(menu):
    if menu < 1 or menu > 4:
        return 1
    else:
        return 0

menu = 0
while menu != 4:
    print_menu()
    menu = int(input("Choose menu: "))
    if check_menu(menu):
        print("Wrong input")
    elif menu != 4:
        print("Menu ", menu, "selected")