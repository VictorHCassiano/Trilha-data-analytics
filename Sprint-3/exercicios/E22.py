class Pessoa:
    def __init__(self,id,nome=None):
        self.__nome = nome
        self.id = id
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
pessoa = Pessoa(1)
pessoa.nome = "João"
print(pessoa.nome)





    
