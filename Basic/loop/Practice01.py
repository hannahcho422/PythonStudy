stop = int(input("어디까지 더할 것인지 입력: "))

i = 1
sum = 0

while i <= stop :
    sum = sum + i
    i += 1

print("1부터 ", stop, "까지의 정수 합 = ", sum)