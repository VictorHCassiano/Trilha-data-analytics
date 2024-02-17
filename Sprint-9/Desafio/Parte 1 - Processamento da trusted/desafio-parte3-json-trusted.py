from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import input_file_name, regexp_extract, to_date
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, DoubleType, ArrayType, DateType, LongType
from awsglue.utils import getResolvedOptions
import sys
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

output_path =  args['S3_TARGET_PATH']
json_file_path = args['S3_INPUT_PATH']




df_raw = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
          
           json_file_path
        ]
    },
    "json",
).toDF()


df_raw = df_raw.withColumn("release_date", to_date(df_raw["release_date"], "yyyy-MM-dd"))

df_raw = df_raw.withColumn("file_path", input_file_name())
df_raw = df_raw.withColumn("collect_date", regexp_extract(df_raw["file_path"], r"(\d{4}/\d{2}/\d{2})", 1))

df_trusted = df_raw.dropna()


df_trusted_dynamic = DynamicFrame.fromDF(df_trusted, glueContext, "df_trusted")

glueContext.write_dynamic_frame.from_options(
    frame = df_trusted_dynamic,
    connection_type = "s3",
    connection_options = {"path": output_path, "partitionKeys": ["collect_date"]},
    format = "parquet"
)
job.commit()