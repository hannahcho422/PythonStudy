# Room number

import math

room = input("Enter the room number: ")

room_num = [0] * 10

for i in room:
    if i == '9':
        room_num[6] += 1
    else:
        room_num[int(i)] += 1

room_num[6] = math.ceil((room_num[6]) / 2)

print(max(room_num))