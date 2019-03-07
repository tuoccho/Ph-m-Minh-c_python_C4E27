ls = [5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my sheep size")
print(ls)
for i in range(3):
    print("MONTH ",i+1)
    ls = [x + 50 for x in ls]
    print("One month has passed, now here is my flock")
    print(ls)
    print("Now my biggest sheep has size",max(ls),"let's shear it")
    a = ls.index(max(ls))
    ls[a] = 8
    print("After Shearing, here is my flock")
    print (ls)
print('My flock has size in total: ', sum(ls))
print('I would get', sum(ls), '* 2 = ', sum(ls) * 2)









    # print("Now my biggest sheep has size",max(ls),"let's shear it")
    # ls.remove(max(ls))
    # print("After Shearing, here is my flock")
    # print (ls)
    # ls = [x + 50 for x in ls]
    # print("One month has passed, now here is my flock")
    # print(ls)
