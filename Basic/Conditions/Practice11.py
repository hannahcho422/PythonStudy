work_hour = int(input("Enter your work hour: "))
hourly_pay = int(input("Enter your hourly pay: "))

if (work_hour > 40):
    weekly_pay = 1.5 * hourly_pay * (work_hour - 40) + hourly_pay * 40
    print("Total pay: ", weekly_pay)
else:
    weekly_pay = hourly_pay * work_hour
    print("Total pay: ", weekly_pay)