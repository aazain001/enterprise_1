# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "03bc838f-e5a7-4d46-b6ae-925732006366",
# META       "default_lakehouse_name": "lh_gold",
# META       "default_lakehouse_workspace_id": "0dbe079c-f93a-46ab-9084-c25fa1ddc87e",
# META       "known_lakehouses": [
# META         {
# META           "id": "03bc838f-e5a7-4d46-b6ae-925732006366"
# META         },
# META         {
# META           "id": "1af4247c-150f-420b-b2b7-c73863789714"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

print("Building Gold Dimension: dim_customers...")
# Read explicitly using schema-qualified names
df_customers = spark.read.table("lh_silver.dbo.silver_customers")
df_orders = spark.read.table("lh_silver.dbo.silver_orders")

# Aggregate order metrics per customer
df_cust_metrics = df_orders.groupBy("customer_id").agg(
    F.count("order_id").alias("total_orders"),
    F.sum("quantity").alias("total_items_purchased"),
    F.max("order_date").alias("last_order_date")
)

# Join back to customer profile
dim_customers = df_customers.join(df_cust_metrics, on="customer_id", how="left") \
                            .fillna({"total_orders": 0, "total_items_purchased": 0})

# Write to lh_gold tables (saving to default schema dbo in lh_gold)
dim_customers.write.mode("overwrite").format("delta").saveAsTable("dim_customers")
print("dim_customers written successfully!")


print("Building Gold Fact: fact_sales...")
# Create a clean sales fact table joining orders and customer info
fact_sales = df_orders.join(df_customers.select("customer_id", "address"), on="customer_id", how="inner") \
                      .select(
                          "order_id",
                          "customer_id",
                          "product_id",
                          "quantity",
                          "order_date",
                          "status",
                          "address"
                      )

fact_sales.write.mode("overwrite").format("delta").saveAsTable("fact_sales")
print("fact_sales written successfully!")

print("All Gold layer models created successfully!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
