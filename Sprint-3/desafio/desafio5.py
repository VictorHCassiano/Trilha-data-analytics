#Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.Ao escrever no arquivo, considere o padrão de saída <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.

with open('actors.csv') as arquivo:
    next(arquivo)
    atores = []
    gross_total = []
    for registro in arquivo:
        dados = registro
        x = dados.replace(", ", " ") 
        x =  x.strip().split(',')
        atores.append(x[0])
        gross_total.append(float(x[5]))


atores_gross = list(zip(atores, gross_total))


for i in range(len(atores_gross)):
    for j in range(len(atores_gross) - i - 1):
        if atores_gross[j][1] < atores_gross[j + 1][1]:
            atores_gross[j], atores_gross[j + 1] = atores_gross[j + 1], atores_gross[j]


with open('etapa-5.txt', 'w') as arquivo_saida:
    for ator, gross in atores_gross:
        arquivo_saida.write(f'{ator} - {gross}\n')
   
    

    