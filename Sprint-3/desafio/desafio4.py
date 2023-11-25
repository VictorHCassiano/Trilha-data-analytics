#A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do  filme. Ao escrever no arquivo, considere o padrão de saída <sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, adicionando um resultado a cada linha.


with open('actors.csv') as arquivo:
    next(arquivo)
    filmes =[]
    for registro in arquivo:
        dados = registro
        x = dados.replace(", ", " ") 
        x =  x.strip().split(',')
        filmes.append(x[4])


filmes_unicos = set(filmes)

contagem_filme = []

for filme in filmes_unicos:
    contagem = filmes.count(filme)
    contagem_filme.append((filme, contagem))


for i in range(len(contagem_filme)):
    for j in range(len(contagem_filme) - i - 1):
        if contagem_filme[j][1] < contagem_filme[j + 1][1]:
            contagem_filme[j], contagem_filme[j + 1] = contagem_filme[j + 1], contagem_filme[j]


with open('etapa-4.txt', 'w') as arquivo:
    for filme, contagem in contagem_filme:
        arquivo.write(f'O filme {filme} aparece {contagem} vez(es) no dataset\n')
 




 
        
