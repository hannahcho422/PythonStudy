# 합계 구하기

stop = int(input("Enter the upper bound of the summation: "))

sum = 0

for i in range(1, stop + 1) :
    sum += i

print("The sum from 1 to ", stop, " = ", sum)