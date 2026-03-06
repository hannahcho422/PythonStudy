# List practice

List = []

for i in range(5) :
    integer = int(input("Enter 5 integers: "))
    List.append(integer)
    
print(List)
print("Average: ", sum(List) / 5)
