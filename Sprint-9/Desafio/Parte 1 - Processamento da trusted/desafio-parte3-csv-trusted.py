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
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

output_path =  "s3://buckerdesafioetl/Trusted/"




df_raw = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            "s3://buckerdesafioetl/Raw/Local/CSV/2024/01/18/"
        ],
        "separator": "|"
    },
    "csv",
).toDF()

df_trusted = df_raw.dropna()

df_trusted_dynamic = DynamicFrame.fromDF(df_trusted, glueContext, "df_trusted")


glueContext.write_dynamic_frame.from_options(
    frame = df_trusted_dynamic,
    connection_type = "s3",
    connection_options = {"path": output_path},
    format = "parquet"
)
job.commit()