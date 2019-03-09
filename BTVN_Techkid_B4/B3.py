print('Answer the following algebra question: ')
print('if x = 8, then what is the value of 4(x + 3)')
data = {
    "1.": 35,
    "2.": 36,
    "3.": 40,
    "4.": 44
}
for i in data:
    print(i, data[i])
nhap = int(input('Ur choice:'))
if nhap == 4:
    print('Bingo')
else:
    print(':(')