# Databricks notebook source
from pyspark.sql.functions import col, trim

# ============================================================
# 1. CUSTOMERS
# Bronze → Silver
# ============================================================

customers_cleaned = (
    spark.table("ops.bronze.customers_raw")
    .dropDuplicates() #Remove duplicate rows
    .filter(col("customer_id").isNotNull()) #Remove records where customer_id is NULL
    .withColumn("name", trim(col("name"))) #Clean the customer name
    .withColumn("email", trim(col("email"))) #Clean the email
)

customers_cleaned.write.mode("overwrite").saveAsTable(
    "ops.silver.customers_cleaned"
)


# ============================================================
# 2. TRANSACTIONS
# Bronze → Silver
# ============================================================

transactions_cleaned = (
    spark.table("ops.bronze.transactions_raw")
    .dropDuplicates()
    .filter(col("transaction_id").isNotNull())
    .filter(col("customer_id").isNotNull())
)

transactions_cleaned.write.mode("overwrite").saveAsTable(
    "ops.silver.transactions_cleaned"
)


# ============================================================
# 3. ACCOUNTS
# Bronze → Silver
# ============================================================

accounts_cleaned = (
    spark.table("ops.bronze.accounts_raw")
    .dropDuplicates()
    .filter(col("account_id").isNotNull())
    .withColumn("account_name", trim(col("account_name")))
)

accounts_cleaned.write.mode("overwrite").saveAsTable(
    "ops.silver.accounts_cleaned"
)


# ============================================================
# 4. OPPORTUNITIES
# Bronze → Silver
# ============================================================

opportunities_cleaned = (
    spark.table("ops.bronze.opportunities_raw")
    .dropDuplicates()
    .filter(col("opportunity_id").isNotNull())
    .filter(col("account_id").isNotNull())
    .withColumn("opportunity_name", trim(col("opportunity_name")))
)

opportunities_cleaned.write.mode("overwrite").saveAsTable(
    "ops.silver.opportunities_cleaned"
)


# ============================================================
# 5. LEADS
# Bronze → Silver
# ============================================================

leads_cleaned = (
    spark.table("ops.bronze.leads_raw")
    .dropDuplicates()
    .filter(col("lead_id").isNotNull())
    .withColumn("company_name", trim(col("company_name")))
    .withColumn("contact_name", trim(col("contact_name")))
    .withColumn("email", trim(col("email")))
)

leads_cleaned.write.mode("overwrite").saveAsTable(
    "ops.silver.leads_cleaned"
)


print("Silver cleansing completed successfully!")

# COMMAND ----------

spark.sql("SHOW TABLES IN ops.silver").show()