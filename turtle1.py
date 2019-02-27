from turtle import *

shape("turtle")
speed(0)
color('red')
begin_fill
for i in range(4):
    left(30)
    forward(70)
    right(60)
    forward(70)
    right(120)
    forward(70)
    right(60)
    forward(70)
    right(60)
end_fill

mainloop()