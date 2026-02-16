credits = int(input("Enter credits taken: "))
gpa = float(input("Enter gpa: "))

if credits >= 140 and gpa >= 2.0 :
    print("Graduation approved.")
else :
    print("Graduation rejected.")