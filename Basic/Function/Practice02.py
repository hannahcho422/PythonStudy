# Return greater number

def get_max(a, b) :
    if a > b :
        return a
    elif a < b :
        return b
    else :
        print("Same number")

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

print("Greater integer: ", get_max(num1, num2))