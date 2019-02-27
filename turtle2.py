from turtle import *

shape("turtle")
speed(0)

color("blue")
begin_fill
for i in range(3):
    forward(100)
    left(120)
for i in range(5):
    forward(100)
    left(72)
end_fill

color("red")
begin_fill
for i in range(4):
    forward(100)
    left(90)
for i in range(6):
    forward(100)
    left(60)
end_fill

mainloop()