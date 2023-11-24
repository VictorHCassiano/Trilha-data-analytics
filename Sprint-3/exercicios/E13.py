def my_map(list,f):
    b = []
    for x in list:
        b.append(f(x))
    print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = my_map(a, lambda x: x * x)