# 누적합계가 1000이상이 되는 시점

sum = 0
count = 0

for i in range(1, 101):
    sum += i
    count += 1
    
    if sum >= 1000 :
        print(count)
        break
