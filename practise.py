from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

spark = SparkSession \
    .builder \
    .appName("Python PySpark Example") \
    .getOrCreate()

column_names = ["language", "framework", "users"]
data = [
    ("Python", "Django", 20000),
    ("Python", "FastAPI", 9000),
    ("JavaScript", "ReactJS", 5000)
]
df = spark.createDataFrame(data, column_names)
df.show()

# Define Python function
def lower_case(text: str) -> str:
    return text.lower()


#help(udf)
# Convert Python function into UDF
lower_case_udf = udf(
    lambda x: lower_case(x),StringType())

# Apply UDF to DataFrame
new_df = df.withColumn(
    "framework_lower",
    lower_case_udf(col("framework"))
)
new_df.show()





