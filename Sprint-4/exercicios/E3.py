from  functools import reduce
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

def calcula_saldo(lancamentos) -> float:
    lista_retorno =  list(map(lambda x : x[0] if x[1] == 'C' else -x[0],lancamentos))
    
    soma_retorno = reduce(lambda x,y: y+x,lista_retorno)
    return soma_retorno

print(calcula_saldo(lancamentos))