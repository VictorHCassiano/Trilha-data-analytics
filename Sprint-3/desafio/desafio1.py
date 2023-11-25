#Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.
maior_numero_filmes = 0
actor_maior_numero_filmes = ''
with open('actors.csv') as arquivo:
    next(arquivo)
    for registro in arquivo:
        dados = registro
        x = dados.replace(", ", " ") 

        x =  x.strip().split(',')

        numero_filmes = int(x[2])
        if numero_filmes > maior_numero_filmes:
            maior_numero_filmes = numero_filmes
            actor_maior_numero_filmes = x[0]
        
arquivo.close()
with open('etapa-1.txt','w') as arquivo2:
    arquivo2.write('O ator com maior número de filmes é {} com {} filmes'.format(actor_maior_numero_filmes, maior_numero_filmes))
    arquivo2.close()
       