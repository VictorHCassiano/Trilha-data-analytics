
with open("number.txt") as arquivo:
      numeros = list(map(lambda x: x.strip(), arquivo.readlines()))
      

ordenar = sorted(numeros, key = lambda x: int(x), reverse=True)
ordernar_int = list(map(lambda x: int(x), ordenar))

filtro_npar = list(filter(lambda x: int(x) % 2 == 0, ordernar_int))


print(filtro_npar[:5])
soma = sum(map(lambda x: int(x), filtro_npar[:5]))
print(soma)

