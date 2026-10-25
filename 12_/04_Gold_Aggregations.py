# Databricks notebook source
from pyspark.sql.functions import (
    col,
    sum,
    count,
    avg,
    when,
    round
)

# ============================================================
# 1. CUSTOMER SPENDING
# Silver: customer_transactions
# Gold:   customer_spending
# ============================================================

customer_transactions = spark.table(
    "ops.silver.customer_transactions"
)

customer_spending = (
    customer_transactions
    .groupBy(
        "customer_id",
        "name",
        "customer_segment"
    )
    .agg(
        sum("amount").alias("total_spending"),
        count("transaction_id").alias("transaction_count"),
        avg("amount").alias("average_transaction_amount")
    )
    .withColumn(
        "total_spending",
        round(col("total_spending"), 2)
    )
    .withColumn(
        "average_transaction_amount",
        round(col("average_transaction_amount"), 2)
    )
)

customer_spending.write.mode("overwrite").saveAsTable(
    "ops.gold.customer_spending"
)


# ============================================================
# 2. ACCOUNT PERFORMANCE
# Silver: account_opportunities
# Gold:   account_performance
# ============================================================

account_opportunities = spark.table(
    "ops.silver.account_opportunities"
)

account_performance = (
    account_opportunities
    .groupBy(
        "account_id",
        "account_name",
        "industry"
    )
    .agg(
        sum("amount").alias("total_opportunity_value"),
        count("opportunity_id").alias("opportunity_count"),
        avg("amount").alias("average_opportunity_value")
    )
    .withColumn(
        "total_opportunity_value",
        round(col("total_opportunity_value"), 2)
    )
    .withColumn(
        "average_opportunity_value",
        round(col("average_opportunity_value"), 2)
    )
)

account_performance.write.mode("overwrite").saveAsTable(
    "ops.gold.account_performance"
)


# ============================================================
# 3. SALES PIPELINE SUMMARY
# Silver: leads_cleaned
# Gold:   sales_pipeline_summary
# ============================================================

leads_cleaned = spark.table(
    "ops.silver.leads_cleaned"
)

sales_pipeline_summary = (
    leads_cleaned
    .groupBy("status")
    .agg(
        count("lead_id").alias("lead_count"),
        round(avg("lead_score"), 2).alias("average_lead_score")
    )
    .orderBy("status")
)

sales_pipeline_summary.write.mode("overwrite").saveAsTable(
    "ops.gold.sales_pipeline_summary"
)


print("Gold aggregations completed successfully!")

# COMMAND ----------

spark.sql("SHOW TABLES IN ops.gold").show()