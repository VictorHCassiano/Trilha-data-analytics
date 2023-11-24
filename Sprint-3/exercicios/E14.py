def arrayinfinito(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(kwargs[i])

arrayinfinito(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

