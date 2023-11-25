#Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna Avarage per Movie para fins de cálculo.
maior_avg_media = 0
ator = ''
with open('actors.csv') as arquivo:
    next(arquivo)
    for registro in arquivo:
        dados = registro
        x = dados.replace(", ", " ") 

        x =  x.strip().split(',')
       
        avg_media = float(x[3])
        
        if avg_media > maior_avg_media:
            maior_avg_media = avg_media
            ator = x[0]

arquivo.close()

with open('etapa-3.txt','w') as arquivo2:
    arquivo2.write('O ator com a maior média de receita de bilheteria bruta por filme é {} com {}'.format(ator,round(maior_avg_media,2)))
    arquivo2.close()

