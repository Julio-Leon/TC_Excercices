import pyspark
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, avg

print(pyspark.__version__)


spark = pyspark.sql.SparkSession.builder.appName("Big Data").getOrCreate()

big_data = spark.read.csv("transactions_large.csv", header=True, inferSchema=True)

big_data.write.mode("overwrite").partitionBy("transaction_date").parquet("output/transaction_data")

employees = spark.read.csv("employees.csv", header=True, inferSchema=True)
department = spark.read.csv("departments.csv", header=True, inferSchema=True)
students = spark.read.csv("students.csv", header=True, inferSchema=True)

window_spec = Window.partitionBy("department").orderBy("salary")

employees = employees.withColumn("rank", rank().over(window_spec))

window_spec_2 = (
    Window
    .orderBy("transaction_date")
    .rowsBetween(-2, 0)
)

big_data = big_data.withColumn("rolling_avg_amount", avg("amount").over(window_spec_2))

big_data.show()
employees.show()