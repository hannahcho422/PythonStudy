# 빈 우유병 3개 -> 새 우유 1병
# 우유 1병: 300원
# 현금 24300원으로 우유 모두 몇 병 마실 수 있음?
# while문

bottle_price = int(input("Enter the price of a bottle: "))
cash = int(input("Enter the total amount of cash: "))

initial = cash // bottle_price
total = initial
empty = initial

while empty >= 3:
    new_milk = empty // 3
    total = total + new_milk
    empty = (empty % 3) + new_milk

print("Total number of bottles drunk: ", total)



