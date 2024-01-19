import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import upper
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_file
]
},
"csv",
{"withHeader": True, "separator":","},
)

spark_df = df.toDF()

from pyspark.sql import functions as F


female_df = spark_df.filter(spark_df['sexo'] == 'F').groupBy('nome', 'ano').agg(F.count('nome').alias('contagem')).orderBy('contagem', ascending=False)


top_female_name = female_df.first()

print(f"O nome feminino com mais registros foi {top_female_name['nome']} e ocorreu no ano {top_female_name['ano']}.")


male_df = spark_df.filter(spark_df['sexo'] == 'M').groupBy('nome', 'ano').agg(F.count('nome').alias('contagem')).orderBy('contagem', ascending=False)


top_male_name = male_df.first()

print(f"O nome masculino com mais registros foi {top_male_name['nome']} e ocorreu no ano {top_male_name['ano']}.")



spark_df.write.partitionBy('sexo', 'ano').json('s3://etlawsglue/lab4-glue/frequencia_registro_nomes_eua')

grouped_df = spark_df.groupBy('ano', 'sexo').agg(F.count('nome').alias('contagem')).orderBy('ano', ascending=False)

grouped_df.show()

spark_df = spark_df.withColumn('nome', upper(spark_df['nome']))

spark_df.show()

glueContext.write_dynamic_frame.from_options(
frame = df,
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet")
job.commit()
