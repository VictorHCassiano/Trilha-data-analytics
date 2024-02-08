
import requests
import json
import boto3
import os
from datetime import datetime

AWS_ACCESS_KEY_ID="ASIAQOP23LSGWLR5ZOHD"
AWS_SECRET_ACCESS_KEY="bYhfqbY+sR/fOimOuxp9F9NUg4sCxk7O521e7KwX"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEIT//////////wEaCXVzLWVhc3QtMSJGMEQCIExj6bn9UPeCnTYb5H9b/RfyPp7jGtIElzz+LCurNiR7AiBxGWPznJZQvbNC/dnxvlhcUPGkwPEWWWFfnSijWRWIGiqjAwhNEAAaDDAzMTEyNzcyMzE0OSIM50G5TFXemBRu6EM3KoADyVuI20iJfxFu6dGNRgxHag3xFctit7i99dU7uFmOw0Z1X9c4BeQR7NBtZcuqnlZja7m6Wxhq71UX2cAVQxSVqL3H2uioa9FnW8TDpk36eCwUdnw0qMWh8ppJIxpDbOyMusu9POfQX7iKNetPp7ymFPQteX/x+zl2b/tqz8BO79gi8Dc5VubPrNETU9zTQ9WK+YAYTBwV95YoPSEBkao2y9EioVCUO/T2k5TtgLPcmdC6ZqGlkfiFgxQnu3wCkk26+x78o0tlgB9rV08qspekVY5pN4f2dw6hjfwOLkV8FS19ULBhD+YrHDsLpHut4T4/3Vew7BCyatKSHJ+Jb0Z0DYhVDFNA+6xlxCswk8pOJgTPg7gnbVz9RBsEfW9pYpkMd6mH5NrHIcYM2OaTNWuKSbLyPIzGfgKLvBy20zqWlihtvlv2KzWcDwdpllq+wqlxIXDpDwvEXkvdyi7VrNHhDDrLfDGb2S95+rLBDSy9kSvgp08Op/W9rW9+TOUhbe4aMNbs760GOqcBDFXwy9OYbKl/+NDybI2dulEue0xyatpbmgppWFQ8IAMdByrNAOpK6cJaUag228qSwWvp0yXc5wQkHJL47YWpEvObBiFKZ2liodcBuwDw/c4bWSXzbZLPIYGpg3oK3G/81F3CgbKYunACrDZD35hoh1jUS/6Kd+v60fGaEypytPHdTZt04jij84e9ybjDpF5yaCTWJMtA0ZoyU7A+u2gzenz5/90Oauo="
def lambda_handler(event, context):
    chave_api = "150eb015d61e7f55617a13a1cc4a9aea"
    id_colecao = "87096"  

    resposta_colecao = requests.get(f"https://api.themoviedb.org/3/collection/{id_colecao}?api_key={chave_api}")
    dados_colecao = resposta_colecao.json()

    todos_dados_filme = []


    id_drama = 18
    for pagina in range(1, 6):  
        resposta_filmes = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={chave_api}&with_genres={id_drama}&page={pagina}")
        filmes = resposta_filmes.json()
        for filme in filmes['results']:
            id_filme = filme['id']
            resposta_filme = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={chave_api}")
            dados_filme = resposta_filme.json()
            filme['budget'] = dados_filme['budget']
            filme['revenue'] = dados_filme['revenue']
            todos_dados_filme.append(filme)
  

    for filme in dados_colecao['parts']:
        id_filme = filme['id']

        resposta_filme = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={chave_api}")
        dados_filme = resposta_filme.json()

        resposta_similar = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme}/similar?api_key={chave_api}")
        dados_similar = resposta_similar.json()

        for filme_similar in dados_similar['results']:
            id_filme_similar = filme_similar['id']
            resposta_filme_similar = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme_similar}?api_key={chave_api}")
            dados_filme_similar = resposta_filme_similar.json()
            filme_similar['budget'] = dados_filme_similar['budget']
            filme_similar['revenue'] = dados_filme_similar['revenue']

        resposta_recomendacoes = requests.get(f"https://api.themoviedb.org/3/movie/{id_filme}/recommendations?api_key={chave_api}")
        dados_recomendacoes = resposta_recomendacoes.json()

        for recomendacao in dados_recomendacoes['results']:
            id_recomendacao = recomendacao['id']
            resposta_recomendacao = requests.get(f"https://api.themoviedb.org/3/movie/{id_recomendacao}?api_key={chave_api}")
            dados_recomendacao = resposta_recomendacao.json()
            recomendacao['budget'] = dados_recomendacao['budget']
            recomendacao['revenue'] = dados_recomendacao['revenue']

        todos_dados_filme.append({
            "detalhes_filme": dados_filme,
            "filmes_similares": dados_similar,
            "recomendacoes": dados_recomendacoes
        })
            
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