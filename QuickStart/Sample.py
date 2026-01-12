from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQLExample").getOrCreate()

df = spark.createDataFrame(
    [{"Google": "Colab", "Spark": "Scala"}, {"Google": "Dataproc", "Spark": "Python"}]
)
df.show()
