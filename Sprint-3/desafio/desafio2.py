#Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média da coluna Gross.
contador = 0
gross_total = 0
with open('actors.csv') as arquivo:
    next(arquivo)
    for registro in arquivo:
        dados = registro
        x = dados.replace(", ", " ") 

        x =  x.strip().split(',')
       
        gross_total += float(x[5])
        contador += 1

media_gross = gross_total/contador
arquivo.close()

with open('etapa-2.txt','w') as arquivo2:
    arquivo2.write('A média de receita de bilheteria bruta dos principais filmes é {}'.format(round(media_gross,2)))
    arquivo2.close()