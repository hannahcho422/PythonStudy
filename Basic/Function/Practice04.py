# Finding multiples
# 입력값 존재, 반환값 없음

def mul(n, max_num):
    if n >= max_num :
        print("Wrong input")
    else :       
        for i in range(1, max_num + 1) :
            if i % n == 0 :
                print(i)
            

multiple = int(input("Enter the multiple: "))
max_number = int(input("Enter the maximum number: "))

mul(multiple, max_number)

'''
def mul(n, max_num):
    if n >= max_num:
        print("Wrong input")
    else:
        for i in range(n, max_num + 1, n):
            print(i)
'''