#etapa1
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, udf
from pyspark.sql.types import StringType, IntegerType
import random
from pyspark.sql.functions import floor
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt")
df_nomes = df_nomes.withColumnRenamed("_c0", "nomes")
#etapa2


df_nomes = df_nomes.withColumn("Escolaridade", 
                               when(rand() < 0.33, "Fundamental")
                               .when(rand() < 0.66, "Medio")
                               .otherwise("Superior"))
#etapa3



paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]
#etapa4

df_nomes = df_nomes.withColumn("random_index", (rand() * len(paises)).cast(IntegerType()))


def index_to_country(index):
    return paises[index]

index_to_country_udf = udf(index_to_country, StringType())


df_nomes = df_nomes.withColumn("Pais", index_to_country_udf(df_nomes["random_index"]))


df_nomes = df_nomes.drop("random_index")


df_nomes = df_nomes.withColumn("random", rand())


df_nomes = df_nomes.withColumn("AnoNascimento", floor(df_nomes["random"] * (2010 - 1945 + 1) + 1945))
#etapa5

df_nomes = df_nomes.drop("random")


df_select = df_nomes.filter(df_nomes["AnoNascimento"] > 2000)

df_select.show(10)

df_nomes.createOrReplaceTempView("pessoas")
#etapa6

df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento > 2000")
#etapa7

millennials_count = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).select("AnoNascimento").count()

print(millennials_count)
#etapa8


millennials_count_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")

millennials_count_sql.show()
#etapa9

generation_counts = spark.sql("""
SELECT 
    Pais,
    CASE
        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
        WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        ELSE 'Other'
    END AS Geracao,
    COUNT(*) as Quantidade
FROM 
    pessoas
GROUP BY 
    Pais, Geracao
ORDER BY 
    Pais ASC, Geracao ASC, Quantidade ASC
""")
#etapa10


generation_counts.show()
df_nomes.show(10)
df_select.show(10)