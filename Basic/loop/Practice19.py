# Addition excluding multiples of 3

sum = 0

for i in range (1, 101):
    if i % 3 == 0 :
        continue
    '''
    else: 
        sum += i
    '''
    sum += i
print("Sum of 1 to 100 exluding multiples of 3: ", sum)