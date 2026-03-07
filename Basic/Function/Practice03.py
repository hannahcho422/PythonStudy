# Return distance
# 입력값 없음, 반환값 존재

def distance():
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    return (x**2 + y**2) ** 0.5

print("Distance: ", distance())