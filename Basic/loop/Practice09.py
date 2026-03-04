import turtle

t = turtle.Turtle()
t.shape("turtle")

while True :
    direction = input("Enter the direction(l: left, r: right, q: quit): ")
    
    if direction == "l" :
        t.left(90)
        t.forward(100)
    elif direction == "r" :
        t.right(90)
        t.forward(100)
    else :
        break

turtle.done()