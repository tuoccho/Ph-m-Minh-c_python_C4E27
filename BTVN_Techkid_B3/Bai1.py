Shop = ['T-Shirt','Sweater']
while True:
    a = input("Welcome to our shop, what do you want (C, R, U, D): ")
    if a == 'R':
        print(Shop)
    elif a == 'C':
        b = input("Enter new item: ")
        Shop.append(b)
        print(Shop)
    elif a == 'U':
        vitri = int(input("Update position?: "))
        newitem = str(input("New item?: "))
        if vitri <= len(Shop):
            Shop[vitri-1] = newitem 
            print(Shop)
    elif a == 'D':
        vitridel = int(input("Delete position?: "))
        del Shop[vitridel]
        print(Shop)