# Write a function named is_inside that checks if a point is inside a rectangle,
# takes 2 parameters, 
# the first is a list with 2 elements respectively represents x and y coordinates of the given point, 
# the second is a list with 4 elements respectively represents x, y coordinates and width height of the given rectangle

def is_inside(vitri,hcn):
    if hcn[0] <= vitri[0] <= hcn[0] + hcn[2] and hcn[1] <= vitri[1] <= hcn[1] + hcn[3]:
        return True
    else:
        return False

# vitri = [200,120]
# hcn = [140,60,100,200]

vt_new = []
vtx = int(input('Nhap toa do x: '))
vt_new.append(vtx)
vty = int(input('Nhap toa do y: '))
vt_new.append(vty)

if is_inside(vt_new,[140,60,100,200]):
    print('Diem',vt_new,'nam trong hcn')
else:
    print('Diem',vt_new,' nam ngoai hcn')