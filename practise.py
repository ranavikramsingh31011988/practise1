from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, ltrim, rtrim

# Initialize Spark session
spark = SparkSession.builder.appName("TrimExample").getOrCreate()

# Sample Data
data = [("  Hello  ",), ("  World",), ("Spark  ",)]
columns = ["col1"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Apply trim functions
df_trimmed = df.select(
    df.col1,
    trim(df.col1).alias("trimmed"),
    ltrim(df.col1).alias("left_trimmed"),
    rtrim(df.col1).alias("right_trimmed")
)

df_trimmed.show(truncate=False)

print("this is new file")