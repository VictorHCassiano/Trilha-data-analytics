from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, length

spark = SparkSession.builder.appName("Contador de Palavras").getOrCreate()

df = spark.read.text("README.md")

palavras = df.select(explode(split(df.value, "\\s+")).alias("palavras"))


palavras = palavras.filter(length(col("palavras")) > 0)

contarPalavras = palavras.groupBy("palavras").count()

contarPalavras_ordenado = contarPalavras.sort(col("count").desc())

contarPalavras_ordenado.show()