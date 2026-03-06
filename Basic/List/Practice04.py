# List method

students = ['아이유', '폴킴', '황인욱']

students.append('청하')
print("(1)", students)

students[2:2] = ['폴킴']
print("(2)", students)
# idx = students.index('폴킴')
# students.insert(idx, '폴킴')

count = students.count('폴킴')
print("(3)", count)

students.pop(3)
print("(4)", students)
# students.remove('황인욱')

students.pop(1)
print("(5)", students)
# del(students[1])

students.sort(reverse=True)
print("(6)", students)
# students.sort()
# students.reverse()