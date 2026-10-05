import pyspark

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("AdvancedSparkTraining") \
    .master("local[*]") \
    .getOrCreate()

orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)

orders.cache()

orders.show()

orders.filter("price > 299").show()

orders.select("city").show()

orders.groupBy("city").sum("price").explain(True)
orders.groupBy('city').avg('price').show()

orders.join(customers, orders.customer_id == customers.customer_id).explain(True)
# orders.join(customers, 'customer_id').show()

print(spark.conf.get("spark.sql.adaptive.enabled"))
