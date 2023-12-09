lista_resultado_nome = []
lista_resultado_notas = []
lista_resultado_media = []
with open('estudantes.csv') as arquivo:
    for linha in arquivo:
        dados = linha.split(',')
        lista_notas = list(map(lambda x: x.strip(), dados))
        notas = list(map(lambda x: int(x), sorted(lista_notas[1:],reverse=True)))
        notas = sorted(notas, reverse=True)[:3]
        lista_resultado_nome.append(lista_notas[0])
        lista_resultado_notas.append(notas)
        lista_resultado_media.append(round(sum(notas)/len(notas),2))

        
lista_resultado = list(zip(lista_resultado_nome, lista_resultado_notas, lista_resultado_media))
lista_resultado = sorted(lista_resultado, key = lambda x: x[2],reverse=True)

for x in lista_resultado:
    print(f'Nome: {x[0]} Notas: {x[1]} Média: {x[2]}')