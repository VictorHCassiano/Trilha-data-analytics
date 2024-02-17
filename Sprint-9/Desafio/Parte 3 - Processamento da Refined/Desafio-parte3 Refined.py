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


dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "banco de dados desafio", table_name = "collect_date_2024_2f02_2f09")


df = dynamic_frame.toDF()


df = df.withColumn("release_date", col("release_date").cast(DateType()))


df_filmes = df.select("id", "title", "original_title")


df_idioma = df.select("id", "original_language")


df_tempo = df.select(
    col("id"),
    col("release_date").alias("data"),
    year("release_date").alias("ano"),
    month("release_date").alias("mes"),
    dayofmonth("release_date").alias("dia")
)



from pyspark.sql.functions import coalesce, lit


df_filmes_fato = df.select(
    "id", 
    "adult", 
    "popularity", 
    col("vote_average").alias("vote_average"), 
    col("vote_count").alias("vote_count"), 
    "budget", 
    coalesce(col("revenue.int"), lit(0)).cast("bigint").alias("receita")
)


dynamic_frame_filmes = DynamicFrame.fromDF(df_filmes, glueContext, "dynamic_frame_filmes")
dynamic_frame_idioma = DynamicFrame.fromDF(df_idioma, glueContext, "dynamic_frame_idioma")
dynamic_frame_tempo = DynamicFrame.fromDF(df_tempo, glueContext, "dynamic_frame_tempo")
dynamic_frame_filmes_fato = DynamicFrame.fromDF(df_filmes_fato, glueContext, "dynamic_frame_filmes_fato")


glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_filmes, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_filme"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_idioma, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_idioma"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_tempo, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/dim_tempo"}, format = "parquet")
glueContext.write_dynamic_frame.from_options(frame = dynamic_frame_filmes_fato, connection_type = "s3", connection_options = {"path": "s3://buckerdesafioetl/Refined/filmes_fato"}, format = "parquet")