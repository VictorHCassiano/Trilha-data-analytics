import requests
import json
import boto3
import os
from datetime import datetime
from aws_credenciais import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_SESSION_TOKEN
from tmdb_credenciais import chave_api
def lambda_handler(event, context):
    
    id_colecao = "87096"  

    resposta_colecao = requests.get(f"https://api.themoviedb.org/3/collection/{id_colecao}?api_key={chave_api}")
    dados_colecao = resposta_colecao.json()

    todos_dados_filme = []


    id_drama = 18
    for pagina in range(1, 6):  
        resposta_filmes = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={chave_api}&with_genres={id_drama}&sort_by=vote_average.desc&page={pagina}")
        filmes = resposta_filmes.json()
        for filme in filmes['results']:
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