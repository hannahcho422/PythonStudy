integer = int(input("Enter the number predicted: "))

if (integer == 50):
    print("Congrats! You are correct.")
elif (integer > 50):
    print("No. The answer is less than the predicted.")
else:
    print("No. The answer is greater than the predicted.")