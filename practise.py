from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestApp").getOrCreate()

data = [(1, "Alice", 25), (2, "Bob", 30)]
columns = ["ID", "Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()
