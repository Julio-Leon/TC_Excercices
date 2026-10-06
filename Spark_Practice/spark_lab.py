import  pyspark

from pyspark.sql.functions import sum, substring, col
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("AdvancedSparkTraining") \
    .master("local[*]") \
    .getOrCreate()

# orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
# customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
# products = spark.read.csv("products.csv", header=True, inferSchema=True)

# order by name
# customers.groupBy(substring('name', 1, 1).alias('first_letter')).count().orderBy('first_letter').show()


# customers.join(orders, 'customer_id').select('name', 'order_id').show()

# products.join(orders, 'product_id').groupBy('product_name').agg(sum('price').alias('total_price')).orderBy('total_price', ascending=False).show()

# df = customers.join(orders, 'customer_id').join(products, 'product_id')

# df.write.csv("joined_data2.csv", header=True)

# df.show()
# df.describe().show()
# df.printSchema()

data = [
    (101, "John Smith", "IT", "5000", "2026-01-15", "ACTIVE", "New York"),
    (102, "Mary Jones", "HR", "4500", "02/20/2026", "active", "Chicago"),
    (103, "David Lee", "IT", "6500", "2026-03-10", "INACTIVE", "Dallas"),
    (104, "Sara Khan", "Finance", None, "04/05/2026", "ACTIVE", "New York"),
    (105, "Mike Brown", "Finance", "7200", "2026-05-18", None, "Chicago"),
    (106, "Emma Davis", "HR", "4800", "06/25/2026", "ACTIVE", None),
    (107, "Chris Wilson", "IT", "8000", "2026-07-01", "active", "Dallas")
]
 
columns = [
    "employee_id",
    "employee_name",
    "department",
    "salary",
    "join_date",
    "status",
    "city"
]
 
df = spark.createDataFrame(data, columns)
 
# df.show()
# df.printSchema()

df.filter('salary > 4000').show()

df = df.withColumn('yearly_salary', col('salary').cast('integer') * 12)

df.printSchema()

df = df.dropna(subset=['salary', 'yearly_salary'])

df = df.withColumn('join_date', F.coalesce(F.try_to_date('join_date', 'yyyy-MM-dd'), F.try_to_date('join_date', 'MM/dd/yyyy')))

df = df.withColumn('year', F.year('join_date')) \
    .withColumn('month', F.month('join_date')) \
    .withColumn('day', F.dayofmonth('join_date'))

df.filter((col('month') > 3) & (col('year') > 2023)).select('employee_name').show()

df = df.dropna(subset=['status'])

df = df.withColumn('status', F.upper('status'))

df = df.fillna({
    'city': 'USA'
})

df = df.drop('join_date')

df = df.withColumn('salary', F.when(col('yearly_salary') > 70000, 'High').otherwise('Low'))

df.show()

df.groupBy('department').agg(
    F.count("*").alias("employee_count"),
    F.avg("yearly_salary").alias("average_salary"),
    F.max("yearly_salary").alias("maximum_salary"),
    F.min("yearly_salary").alias("minimum_salary"),
    F.sum("yearly_salary").alias("total_salary")
).show()