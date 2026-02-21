import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.penup()   # 펜 올려서 그림 그려지지 않게 함
t.goto(100, 100)
t.write("Positive")
t.goto(100, 0)
t.write("0")
t.goto(100, -100)
t.write("Negative")

t.goto(0, 0)
t.pendown()
s = turtle.textinput("", "Enter a number: ")
n = int(s)

if (n > 0) :
    t.goto(100, 100)
elif (n == 0) :
    t.goto(100, 0)
else :
    t.goto(100, -100)
    
turtle.done()