lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


tamanho = len(lista)/3
if type(tamanho) == float:
    tamanho = int(tamanho) +1

parte1 = lista[:tamanho-1]
parte2 = lista[tamanho-1:tamanho*2-2]
parte3 = lista[tamanho*2-2:tamanho*3-1]

print(parte1,parte2,parte3)
