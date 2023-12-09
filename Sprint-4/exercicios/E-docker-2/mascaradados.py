import hashlib

mascarar= ""
while True:
    
    mascarar = input("Digite a palavra a ser mascarada: ")
    
   
    m = hashlib.sha1()
    m.update(mascarar.encode('utf-8'))
    print(m.hexdigest())