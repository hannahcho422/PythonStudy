# 도깨비 방망이

fee = int(input("Enter the pocket fee: "))
multiple = int(input("Enter the multiple of money: "))
count = int(input("Enter the number of times hitting the bat: "))
required = int(input("Enter the money needed: "))

money = required

for i in range(count):
    money = (money + fee) / multiple

print("Initial asset: ", money)