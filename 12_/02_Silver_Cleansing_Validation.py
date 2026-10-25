# Databricks notebook source
# MAGIC %sql
# MAGIC SHOW TABLES IN ops.silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Check row counts
# MAGIC SELECT 'customers_cleaned' AS table_name, COUNT(*) AS row_count
# MAGIC FROM ops.silver.customers_cleaned
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'transactions_cleaned', COUNT(*)
# MAGIC FROM ops.silver.transactions_cleaned
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'accounts_cleaned', COUNT(*)
# MAGIC FROM ops.silver.accounts_cleaned
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'opportunities_cleaned', COUNT(*)
# MAGIC FROM ops.silver.opportunities_cleaned
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'leads_cleaned', COUNT(*)
# MAGIC FROM ops.silver.leads_cleaned;

# COMMAND ----------

# MAGIC %sql
# MAGIC ---Validate NULL primary keys
# MAGIC SELECT 'customers' AS table_name, COUNT(*) AS null_id_count
# MAGIC FROM ops.silver.customers_cleaned
# MAGIC WHERE customer_id IS NULL
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'transactions', COUNT(*)
# MAGIC FROM ops.silver.transactions_cleaned
# MAGIC WHERE transaction_id IS NULL
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'accounts', COUNT(*)
# MAGIC FROM ops.silver.accounts_cleaned
# MAGIC WHERE account_id IS NULL
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'opportunities', COUNT(*)
# MAGIC FROM ops.silver.opportunities_cleaned
# MAGIC WHERE opportunity_id IS NULL
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC SELECT 'leads', COUNT(*)
# MAGIC FROM ops.silver.leads_cleaned
# MAGIC WHERE lead_id IS NULL;