# Drawing polygons

import turtle

t = turtle.Turtle()
t.shape("turtle")

side_num = int(input("Enter the number of sides of the polygon: "))
length = int(input("Enter the lenght of each side: "))

for i in range(side_num) :
    t.forward(length)
    t.right(360 / side_num)

turtle.done()