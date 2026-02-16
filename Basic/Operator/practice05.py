parking_time = int(input("Enter parking time: "))

unit_time = parking_time // 15

charge = unit_time * 1000

print("Parking charge: ", charge)