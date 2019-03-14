from turtle import *
def draw_square(i,j):
    color(j)
    speed(0)
    for k in range(4):
        forward(i)
        left(90)
    mainloop()

leng = int(input('Nhap do dai: '))
mau = input('Nhap mau (eng): ')
draw_square(leng,mau)