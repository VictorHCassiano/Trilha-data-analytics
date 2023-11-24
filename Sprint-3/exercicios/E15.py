class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada


def main():
    lamp = Lampada()
    lamp.liga()
    print(f'A lampada está ligada? {lamp.esta_ligada()}')
    lamp.desliga()
    print(f'A lampada está ligada? {lamp.esta_ligada()}')

main()