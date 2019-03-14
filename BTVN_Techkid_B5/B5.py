from turtle import *
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range (5):
        right(144)
        forward(length)
    mainloop()

draw_star(20,20,100)
