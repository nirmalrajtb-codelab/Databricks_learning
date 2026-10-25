# Databricks notebook source
from pyspark.sql.functions import *

base_path = "/Volumes/ops/bronze/raw_data"

# Customers
customers = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/customers.csv")
)

customers.write.mode("overwrite").saveAsTable(
    "ops.bronze.customers_raw"
)


# Transactions
transactions = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/transactions.csv")
)

transactions.write.mode("overwrite").saveAsTable(
    "ops.bronze.transactions_raw"
)


# Accounts
accounts = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/accounts.csv")
)

accounts.write.mode("overwrite").saveAsTable(
    "ops.bronze.accounts_raw"
)


# Opportunities
opportunities = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/opportunities.csv")
)

opportunities.write.mode("overwrite").saveAsTable(
    "ops.bronze.opportunities_raw"
)


# Leads
leads = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/leads.csv")
)

leads.write.mode("overwrite").saveAsTable(
    "ops.bronze.leads_raw"
)

# COMMAND ----------

spark.sql("SHOW TABLES IN ops.bronze").show()

# COMMAND ----------

