# 리스트에 저장된 색상으로 원 그리기

import turtle

t = turtle.Turtle()
t.shape("turtle")

color_list = []
for s in range(4):
    color = input("Input color: ")
    color_list.append(color)

for i in range(4):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.forward(50)
    
turtle.done()