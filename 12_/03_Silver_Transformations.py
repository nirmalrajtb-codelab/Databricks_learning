# Databricks notebook source
from pyspark.sql.functions import col

# ============================================================
# 1. CUSTOMER TRANSACTIONS
# customers_cleaned + transactions_cleaned
# ============================================================

customers_cleaned = spark.table(
    "ops.silver.customers_cleaned"
)

transactions_cleaned = spark.table(
    "ops.silver.transactions_cleaned"
)

customer_transactions = (
    customers_cleaned
    .join(
        transactions_cleaned,
        customers_cleaned["customer_id"] ==
        transactions_cleaned["customer_id"],
        "inner"
    )
    .select(
        customers_cleaned["customer_id"],
        customers_cleaned["name"],
        customers_cleaned["email"],
        customers_cleaned["city"],
        customers_cleaned["customer_segment"],
        transactions_cleaned["transaction_id"],
        transactions_cleaned["transaction_date"],
        transactions_cleaned["product"],
        transactions_cleaned["amount"],
        transactions_cleaned["payment_method"],
        transactions_cleaned["status"]
    )
)

customer_transactions.write.mode("overwrite").saveAsTable(
    "ops.silver.customer_transactions"
)


# ============================================================
# 2. ACCOUNT OPPORTUNITIES
# accounts_cleaned + opportunities_cleaned
# ============================================================

accounts_cleaned = spark.table(
    "ops.silver.accounts_cleaned"
)

opportunities_cleaned = spark.table(
    "ops.silver.opportunities_cleaned"
)

account_opportunities = (
    accounts_cleaned
    .join(
        opportunities_cleaned,
        accounts_cleaned["account_id"] ==
        opportunities_cleaned["account_id"],
        "left"
    )
    .select(
        accounts_cleaned["account_id"],
        accounts_cleaned["account_name"],
        accounts_cleaned["industry"],
        accounts_cleaned["city"],
        accounts_cleaned["employees"],
        accounts_cleaned["annual_revenue"],
        accounts_cleaned["account_status"],
        opportunities_cleaned["opportunity_id"],
        opportunities_cleaned["opportunity_name"],
        opportunities_cleaned["stage"],
        opportunities_cleaned["amount"],
        opportunities_cleaned["close_date"],
        opportunities_cleaned["sales_rep"]
    )
)

account_opportunities.write.mode("overwrite").saveAsTable(
    "ops.silver.account_opportunities"
)


print("Silver transformations completed successfully!")

# COMMAND ----------

spark.sql("SHOW TABLES IN ops.silver").show()

# COMMAND ----------

spark.table("ops.silver.customer_transactions").show(10)

# COMMAND ----------

spark.table("ops.silver.account_opportunities").show(10)