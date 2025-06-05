import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("PandasToSpark").getOrCreate()

# Create Pandas DataFrame
pdf = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

# Correct way to display Pandas DataFrame
print(pdf)
df = spark.createDataFrame(pdf)

# Show DataFrame
df.show()
