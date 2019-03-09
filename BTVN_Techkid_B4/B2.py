prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for i in prices:
    print('•',i)
    print('• price:', prices[i])
    print('• stock:', stock[i])
    print('')
    value = prices[i] * stock[i]
    total = total + value
print('Tổng tiền bạn có: ',total)