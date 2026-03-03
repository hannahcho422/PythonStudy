# while문 사용해서 입력 받은 정수의 각 자리수 합 계산

integer = int(input("Enter an integer: "))

# 음수 입력 처리
if integer < 0:
    integer = -integer

sum = 0

while integer > 0 :
    last_digit = integer % 10
    sum = sum + last_digit
    integer = integer // 10

print("Sum of the digits of the integer: ", sum)