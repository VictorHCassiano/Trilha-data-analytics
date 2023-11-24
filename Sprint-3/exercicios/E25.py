class Aviao:
    def __init__(self,modelo,velocidade_maxima,cor,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "Azul"
        self.capacidade = capacidade
    def detalhes(self):
        return f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}."


aviao1 = Aviao("BOEING456", 1500, "Azul", 400)
aviao2 = Aviao("Embraer Praetor 600", 863, "Azul", 14)
aviao3 = Aviao("Antonov An-2", 258, "Azul", 12)

lista_avioes = [aviao1, aviao2, aviao3]

for lista in lista_avioes:
    print(lista.detalhes())
       