# 성적 평균 

print("종료하려면 음수를 입력하시오")
grade = int(input("성적을 입력하시오: "))

sum = 0
count = 0

while grade > 0 :
    sum  = sum + grade
    count += 1
    grade = int(input("성적을 입력하시오: "))
    
print("성적의 평균은 ", sum / count)