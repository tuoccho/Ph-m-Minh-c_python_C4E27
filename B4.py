# A. 20 * 1 stars:
# for i in range(0,20): 
    # print("*", end='')
# ------------------------------------------------

# B. n stars (n is entered by users)
# i = int(input("Nhap vao so * ban muon: "))
# for j in range(0,i):
#     print("*", end='')  

# ------------------------------------------------

# C. 9 stars and xs in total
# for i in range(0,4):
#     print("x*", end='')
# print("x")

# ------------------------------------------------

# D. n stars and xs in total (n is entered by users)
# i = int(input("Nhap vao n: "))
# if i%2 == 0:
#     a = int(i/2)
#     for j in range(0,a):
#         print("x*", end='')
# else:
#     b = int((i-1)/2)
#     for k in range(0,b):
#         print("x*", end='')
#     print("x")

# -------------------------------------------------

# F. 7 * 3 stars
# for j in range(0,3):
#     for i in range(0,7): 
#         print("* ", end='')
#     print()

# -------------------------------------------------

m = int(input("Enter m: "))
n = int(input("Enter n: "))
for j in range(0,n):
    for i in range(0,m): 
        print("* ", end='')
    print()

# -------------------------------------------------   