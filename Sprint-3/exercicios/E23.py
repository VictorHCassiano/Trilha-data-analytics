class Calculo:
    def __init__(self):
        pass   
    def Soma(self,x,y):
        return x+y
        
    def Subtracao(self,x,y):
        return x-y


a = Calculo()

print(f'Somando:{a.Soma(4,5)}')
print(f'Subtraindo:{a.Subtracao(4,5)}')