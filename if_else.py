#Điều kiện lồng là trong 1 câu lệnh if chúng ta lồng thêm 1 câu lệnh if hoặc else ở bên trong khối lệnh con đó
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
if x < y:
    print("x nhỏ hơn y")
else:
    if x > y:
        print("x lớn y")
    else:
        print("x và y bằng nhau")