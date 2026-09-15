# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6cfd449d-fb70-4ba6-b545-1c6d5e589762",
# META       "default_lakehouse_name": "lh_bronze",
# META       "default_lakehouse_workspace_id": "0dbe079c-f93a-46ab-9084-c25fa1ddc87e",
# META       "known_lakehouses": [
# META         {
# META           "id": "6cfd449d-fb70-4ba6-b545-1c6d5e589762"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

# Define scale factors (Millions of rows)
num_customers = 50000
num_orders = 1000000
num_clickstream = 5000000

print("Generating raw customer data files...")
df_customers = spark.range(0, num_customers) \
    .withColumn("customer_id", F.concat(F.lit("CUST-"), F.col("id"))) \
    .withColumn("name", F.concat(F.lit("Customer_"), F.col("id"))) \
    .withColumn("email", F.concat(F.col("customer_id"), F.lit("@ecommerce-mock.com"))) \
    .withColumn("address", F.concat(F.lit("Street_"), (F.rand() * 1000).cast("int"))) \
    .withColumn("registration_date", F.date_sub(F.current_date(), (F.rand() * 730).cast("int"))) \
    .drop("id")

# Write as raw CSV to Lakehouse Files zone
df_customers.coalesce(4).write.mode("overwrite") \
    .option("header", "true") \
    .csv("Files/landing/customers/")


print("Generating raw order data files...")
df_orders = spark.range(0, num_orders) \
    .withColumn("order_id", F.concat(F.lit("ORD-"), F.col("id"))) \
    .withColumn("customer_id", F.concat(F.lit("CUST-"), (F.rand() * num_customers).cast("int"))) \
    .withColumn("product_id", F.concat(F.lit("PROD-"), (F.rand() * 500).cast("int"))) \
    .withColumn("quantity", (F.rand() * 5 + 1).cast("int")) \
    .withColumn("order_date", F.date_sub(F.current_date(), (F.rand() * 365).cast("int"))) \
    .withColumn("status", F.element_at(F.array(F.lit("Completed"), F.lit("Pending"), F.lit("Cancelled")), (F.rand() * 3 + 1).cast("int"))) \
    .drop("id")

# Write as raw CSV to Lakehouse Files zone
df_orders.coalesce(8).write.mode("overwrite") \
    .option("header", "true") \
    .csv("Files/landing/orders/")


print("Generating raw clickstream data files...")
df_clickstream = spark.range(0, num_clickstream) \
    .withColumn("event_id", F.concat(F.lit("EVT-"), F.col("id"))) \
    .withColumn("user_id", F.concat(F.lit("CUST-"), (F.rand() * num_customers).cast("int"))) \
    .withColumn("event_type", F.element_at(F.array(F.lit("page_view"), F.lit("add_to_cart"), F.lit("checkout"), F.lit("click")), (F.rand() * 4 + 1).cast("int"))) \
    .withColumn("timestamp", F.current_timestamp()) \
    .withColumn("page_url", F.concat(F.lit("/page/"), (F.rand() * 50).cast("int"))) \
    .drop("id")

# Write as raw JSON to Lakehouse Files zone
df_clickstream.coalesce(10).write.mode("overwrite") \
    .json("Files/landing/clickstream/")

print("All raw files successfully generated in Files/landing/!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
