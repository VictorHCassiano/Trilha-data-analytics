a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for x in a:
    if x == x[::-1]:
        print(f"A palavra: {x} é um palíndromo")
    else:
        print(f"A palavra: {x} não é um palíndromo")