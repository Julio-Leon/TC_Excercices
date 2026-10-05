import  pyspark

from pyspark.sql.functions import sum
from pyspark.sql.functions import substring
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("AdvancedSparkTraining") \
    .master("local[*]") \
    .getOrCreate()

orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
products = spark.read.csv("products.csv", header=True, inferSchema=True)

# order by name
# customers.groupBy(substring('name', 1, 1).alias('first_letter')).count().orderBy('first_letter').show()


# customers.join(orders, 'customer_id').select('name', 'order_id').show()

# products.join(orders, 'product_id').groupBy('product_name').agg(sum('price').alias('total_price')).orderBy('total_price', ascending=False).show()

df = customers.join(orders, 'customer_id').join(products, 'product_id')

df.write.csv("joined_data2.csv", header=True)

df.show()
df.describe().show()
df.printSchema()