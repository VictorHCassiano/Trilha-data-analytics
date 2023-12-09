def calcular_valor_maximo(operadores, operandos) -> float:
    ope = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
         '%': lambda x,y: x % y,
        '**': lambda x, y: x ** y,
        '//': lambda x, y: x // y
    }
    lista_junta = list(zip(operadores, operandos))
    resultado = []

    for x in range(len(lista_junta) - 1):
        appender = list(map(lambda y: ope[y[0]](y[1][0], y[1][1]), lista_junta))
        resultado.append(appender)

    retorno = max(resultado)
    return max(retorno)

if __name__ == "__main__":
    operadores = ['+','-','*','/','+']
    operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
    print(calcular_valor_maximo(operadores, operandos))