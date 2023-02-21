
import pyspark
from pyspark.sql import SparkContext, SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkPractices') \
                    .getOrCreate()

df = spark.sql(" SELECT * FROM research-and-development-survey-2021-csv.csv")



# spark = SparkSession.builder.enableHiveSupport().getOrCreate()

