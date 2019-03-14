def get_even_list(l):
    lb = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            lb.append(l[i])
    return lb
    
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
