from turtle import *
def draw_square(i,j):
    color(j)
    speed(0)
    for k in range(4):
        forward(i)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
