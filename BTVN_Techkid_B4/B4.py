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
dem = 0
if nhap == 4:
    dem += 1
    print('Bingo')
else:
    print(':(')

print('Estimate this answer (exact calculation not needed):')
print('Jack scored these marks in 5 math tests: 49,81,72,66 and 52, What is the mean?')
data1 = {
    "1.": 'About 55',
    "2.": 'About 65',
    "3.": 'About 75',
    "4.": 'About 85'
}
for j in data1:
    print(j, data1[j])
nhap = int(input('Ur choice:'))
if nhap == 2:
    dem += 1
    print('Bingo')
else:
    print(':(')
print('You correctly answer',dem,'out of 2 questions')