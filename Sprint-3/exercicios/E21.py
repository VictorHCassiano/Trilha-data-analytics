class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(f'{self.nome} está voando...')
    
    def emitirsom(self):
        print(f'{self.nome} emitindo som...')

class Pato(Passaro):
    def __init__(self, nome):
        super().__init__(nome)
    
    def emitirsom(self):
        print("Quack Quack")

class Pardal(Passaro):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirsom(self):
        print("Piu Piu")


a = Pato("Pato")
b = Pardal("Pardal")

a.voar()
a.emitirsom()
b.voar()
b.emitirsom()