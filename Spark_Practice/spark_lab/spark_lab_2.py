import pyspark
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, avg
from pyspark.sql import functions as F

print(pyspark.__version__)


spark = pyspark.sql.SparkSession.builder.appName("Big Data").getOrCreate()

big_data = spark.read.csv("transactions_large.csv", header=True, inferSchema=True)

big_data.write.mode("overwrite").partitionBy("transaction_date").parquet("output/transaction_data")

big_data.write.mode("overwrite").parquet("output/transaction_data")
# big_data.write.mode("overwrite").partitionBy("transaction_date").orc("output/transaction_data")

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


# No logical relationship between big_data and department, joining on transaction_id and id might not make sense
joined_table = big_data.join(department, big_data.transaction_id == department.id)

big_data.show()
employees.show()

joined_table.show()

# Benchamark query performance by running the same aggregation on csv, parquet, and orc files
csv_data = spark.read.csv("transactions_large.csv", header=True, inferSchema=True)
parquet_data = spark.read.parquet("output/transaction_data.parquet")
# orc_data = spark.read.orc("output/transaction_data_orc")

from time import time

start = time()
csv_data.groupBy("transaction_date").agg(F.sum("amount")).show()
print("CSV query time:", time() - start)

start = time()
parquet_data.groupBy("transaction_date").agg(F.sum("amount")).show()
print("Parquet query time:", time() - start)

# start = time()
# orc_data.groupBy("transaction_date").agg(F.sum("amount")).show()
# print("ORC query time:", time() - start)