from datetime import date
nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))

resultado = date.today().year - idade
 
print(resultado+100)