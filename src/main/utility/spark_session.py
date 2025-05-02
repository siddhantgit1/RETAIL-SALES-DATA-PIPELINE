import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.utility.logging_config import *

def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("anusha_Spark")\
        .config("spark.jars", "D:\\my_sql_jar\\mysql-connector-j-9.2.0\\mysql-connector-j-9.2.0.jar") \
        .getOrCreate()
    spark.conf.set("spark.hadoop.io.native.lib.available", "false")
    logger.info("spark session %s",spark)
    return spark

spark_session()