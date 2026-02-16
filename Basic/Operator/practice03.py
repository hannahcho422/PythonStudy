sec = int(input("Enter time in seconds: "))

min = sec // 60
remainder = sec % 60

print(min, "분 ", remainder, "초")