import requests
import json
import boto3
import os
from datetime import datetime

AWS_ACCESS_KEY_ID="ASIAQOP23LSG3ZGIDBVE"
AWS_SECRET_ACCESS_KEY="tAv9yW7LULR5IMGgjQBjO0KiqCpLqYGbrlYEGp/4"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEEMaCXVzLWVhc3QtMSJGMEQCIBBVWHQoRnjJdryK+BmIXDBHYWvZGgwt+Gqk80ywxGQGAiAznsUlG5nuXXYC2kAT79rr7jG5DLrSzxlu6JVsujWzdCqjAwgcEAAaDDAzMTEyNzcyMzE0OSIMAJHg2a6iDK1Iwy8zKoAD2Ugpesh6js4W/TMqxtRhkegokgV7agmUfMH3WYq2WlhvJcNYzTvSRojssoQwn4pniPJWawyoa5kHndk/jsTgUh54MctLQU6ONA3YEXu5n34adLaihXK16YL+yNAGauIBpLliRnYHXgsN1KO7aoEnyvHi40RW56JXz+O1zXysUiPeN+if8NSIjMZBrYoyX5bgzZMOMGym3B0a1h6bbfjLXP6YVpGMetLqFy0QTfgw8T0X00hU7VGC5i8RFucr0GKUKubvNA+n8X45sfI4ILYwQqtU4s/O363ZgTUEtNqLXo3VzI7om0XGQGDik8C+C9lUyupnu67Qm+FoT8iYKKJHK9nCrsB8ECJuBAN7+H2Gfaxj0mMReJbgwVHp5xp/5wtH2G1o/Q137s+EMeWiPtk2oKNJm31vyVq9h/V4r93r1AT1xwCPz0hZcEQ5bEcJaJQs6iWqFm67zHLek8SB/ZfRAjweBigUFnkTfWVH1OnaZgx9x5TgSuT4gq3K7Da3EGR7MPzgma4GOqcBt5CncFE/ZIx/WzK6wAJOvvLRu/VYmrQFTYbrVKt5qtf2A5Jd1Yx2AP0yaGqmkCoXUgYDYzCm+A5NK9RhtwZbdHvYOMrUjczSiTc60sxUL2fk/HqC1O0dwV+Xmg0O1J7ELOycnV0n33njIZSDyQtC2BhbUKnJgNRJpP5tTE0rLT9XMiamkB47LZcbilt1LHs7aucciGJVTeD8/hd8ZW9L74oglElSdJg="

def lambda_handler(event, context):
    chave_api = "150eb015d61e7f55617a13a1cc4a9aea"
     

    todos_dados_filme = []

    id_drama = 18
    
    for pagina in range(1, 26):  
        resposta_filmes = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={chave_api}&with_genres={id_drama}&sort_by=popularity.desc&page={pagina}")
        filmes = resposta_filmes.json()
        for filme in filmes['results']:
            id_filme = filme['id']
            resposta_filme = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={chave_api}")
            dados_filme = resposta_filme.json()
            filme['budget'] = dados_filme['budget']
            filme['revenue'] = dados_filme['revenue']
            todos_dados_filme.append(filme)
  

    
            
    grupos = [todos_dados_filme[i:i+100] for i in range(0, len(todos_dados_filme), 100)]

    for i, grupo in enumerate(grupos):
        nome_arquivo_grupo = f"/tmp/data_{i}.json"
        with open(nome_arquivo_grupo, 'w') as f:
            json.dump(grupo, f, indent=4)

    carregar_arquivos('buckerdesafioetl', '/tmp', 'Raw', 'tmdb', 'JSON')
   
def carregar_arquivos(nome_bucket, caminho_pasta, camada_armazenamento, origem_dado, formato_dado):
    s3 = boto3.client(
        's3',
        aws_access_key_id= AWS_ACCESS_KEY_ID,
        aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
        aws_session_token= AWS_SESSION_TOKEN  
    )

    arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]

    for arquivo in arquivos:
        if arquivo.endswith('.json'):
            data_processamento = datetime.now().strftime('%Y/%m/%d')
            nome_arquivo_s3 = f"{camada_armazenamento}/{origem_dado}/{formato_dado}/{data_processamento}/{arquivo}"
            print(f"Enviando {arquivo} para {nome_bucket}/{nome_arquivo_s3}")
            s3.upload_file(os.path.join(caminho_pasta, arquivo), nome_bucket, nome_arquivo_s3)