import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, year, month, dayofmonth
from pyspark.sql.types import DateType
from pyspark.sql.functions import coalesce, lit


# Inicialize o GlueContext
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Crie um DynamicFrame a partir dos dados brutos
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "banco de dados desafio", table_name = "collect_date_2024_2f02_2f09")

# Transforme os dados para se adequar ao esquema de cada tabela
# (Você precisará ajustar este código para se adequar ao esquema de suas tabelas)
df = dynamic_frame.toDF()

# Converta a string de data para um tipo de data
df = df.withColumn("release_date", col("release_date").cast(DateType()))

# Crie a tabela df_filmes
df_filmes = df.select("id", "title", "original_title")

# Crie a tabela df_idioma
df_idioma = df.select("id", "original_language")

# Crie a tabela df_tempo com as colunas "id", "data", "ano", "mes" e "dia"
df_tempo = df.select(
    col("id"),
    col("release_date").alias("data"),
    year("release_date").alias("ano"),
    month("release_date").alias("mes"),
    dayofmonth("release_date").alias("dia")
)




# Calcule a receita de cada filme
df = df.withColumn("receita", coalesce(col("revenue.int"), col("revenue.long")))

# Adicione a receita como uma nova coluna em df_filmes_fato
df_filmes_fato = df.select(
    "id", 
    "adult", 
    "popularity", 
    col("vote_average").alias("vote_average"), 
    col("vote_count").alias("vote_count"), 
    "budget",
    "receita"
)

# Converta os DataFrames do Spark de volta para DynamicFrames
dynamic_frame_filmes = DynamicFrame.fromDF(df_filmes, glueContext, "dynamic_frame_filmes")
dynamic_frame_idioma = DynamicFrame.fromDF(df_idioma, glueContext, "dynamic_frame_idioma")
dynamic_frame_tempo = DynamicFrame.fromDF(df_tempo, glueContext, "dynamic_frame_tempo")
dynamic_frame_filmes_fato = DynamicFrame.fromDF(df_filmes_fato, glueContext, "dynamic_frame_filmes_fato")

# Escreva os dados transformados de volta para o S3
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_filmes, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_filme"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_idioma, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_idioma"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_tempo, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_tempo"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_filmes_fato, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/filmes_fato"}, format = "parquet")