import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

size = int(input("Enter the size of the house: "))

# 집 몸통 (정사각형)
for i in range(4):
    t.forward(size)
    t.right(90)

# 지붕 만들기
t.left(90)          
t.right(30)
t.forward(size)     
t.right(120)        
t.forward(size)     

t.hideturtle()

turtle.done()