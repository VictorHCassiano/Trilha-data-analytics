def pares_ate(n: int):
    for i in range(2, n + 1,2):
        yield i



if __name__ == '__main__':
    n = int(input('Digite um número: '))
    for i in pares_ate(n):
        print(i, end=' ')
    
    