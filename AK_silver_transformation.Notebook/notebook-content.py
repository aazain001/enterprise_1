# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1af4247c-150f-420b-b2b7-c73863789714",
# META       "default_lakehouse_name": "lh_silver",
# META       "default_lakehouse_workspace_id": "0dbe079c-f93a-46ab-9084-c25fa1ddc87e",
# META       "known_lakehouses": [
# META         {
# META           "id": "1af4247c-150f-420b-b2b7-c73863789714"
# META         },
# META         {
# META           "id": "6cfd449d-fb70-4ba6-b545-1c6d5e589762"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

print("Transforming Customers: Cleaning and deduplicating...")
df_cust = spark.sql("SELECT DISTINCT customer_id, name, email, address, registration_date FROM lh_bronze.dbo.bronze_customers WHERE customer_id IS NOT NULL")
df_cust = df_cust.withColumn("name", F.initcap(F.trim(F.col("name")))) \
                 .withColumn("email", F.lower(F.trim(F.col("email"))))

df_cust.write.mode("overwrite").format("delta").saveAsTable("silver_customers")
print("Silver customers table written successfully!")


print("Transforming Orders: Cleaning and casting...")
df_ord = spark.sql("SELECT DISTINCT order_id, customer_id, product_id, quantity, order_date, status FROM lh_bronze.dbo.bronze_orders WHERE order_id IS NOT NULL")
df_ord = df_ord.withColumn("quantity", F.col("quantity").cast("int")) \
               .withColumn("status", F.initcap(F.trim(F.col("status"))))

df_ord.write.mode("overwrite").format("delta").saveAsTable("silver_orders")
print("Silver orders table written successfully!")


print("Transforming Clickstream: Cleaning timestamps and events...")
df_click = spark.sql("SELECT DISTINCT event_id, user_id, event_type, timestamp, page_url FROM lh_bronze.dbo.bronze_clickstream WHERE event_id IS NOT NULL")
df_click = df_click.withColumn("event_type", F.lower(F.trim(F.col("event_type"))))

df_click.write.mode("overwrite").format("delta").saveAsTable("silver_clickstream")
print("Silver clickstream table written successfully!")

print("All Silver layer transformations completed successfully!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
