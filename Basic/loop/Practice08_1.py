# 두 정수의 합(break 쓰기)

while True:
    num1 = int(input("Enter the first integer: "))
    
    if num1 == 0:
        break
    
    num2 = int(input("Enter the second integer: "))
    print(num1, "+", num2, "=", num1 + num2)

print("0 entered. Break from loop.")