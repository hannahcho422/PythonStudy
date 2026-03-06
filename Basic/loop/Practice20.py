# Sum of a dice

sum = 0
count = 0

for i in range(1, 7):
    for k in range(1, 7):
        sum = i + k
        if sum == 6 :
            count += 1
            print(i, k)

print("The number of cases where the sum of two dice is 6: ", count)
            