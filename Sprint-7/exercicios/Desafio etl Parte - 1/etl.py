import boto3
import os
from credenciaisaws import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, AWS_SESSION_TOKEN 
from datetime import datetime

def carregar_arquivos(nome_bucket, caminho_pasta, camada_armazenamento, origem_dado, formato_dado, ):
    s3 = boto3.client(
        's3',
        aws_access_key_id= AWS_ACCESS_KEY_ID,
        aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
        aws_session_token= AWS_SESSION_TOKEN  
    )

    arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]

    for arquivo in arquivos:
        if arquivo.endswith('.csv'):
            data_processamento = datetime.now().strftime('%Y/%m/%d')
            nome_arquivo_s3 = f"{camada_armazenamento}/{origem_dado}/{formato_dado}/{data_processamento}/{arquivo}"
            print(f"Enviando {arquivo} para {nome_bucket}/{nome_arquivo_s3}")
            s3.upload_file(os.path.join(caminho_pasta, arquivo), nome_bucket, nome_arquivo_s3)

carregar_arquivos('buckerdesafioetl', '.', 'Raw', 'Local', 'CSV')
