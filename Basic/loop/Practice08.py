# 두 정수의 합

num1 = int(input("Enter the first integer: "))

while num1 != 0 :
    num2 = int(input("Enter the second integer: "))
    print(num1, " + " , num2, " = ", num1 + num2)
    num1 = int(input("Enter the first integer: "))

print("0 entered. Break from loop.")