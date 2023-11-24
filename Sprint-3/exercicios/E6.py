b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
array1 = set(a)
array2 = set(b)

resultado = array1.intersection(array2)

print(list(resultado))