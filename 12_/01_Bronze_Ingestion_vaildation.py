# Databricks notebook source
# MAGIC %sql
# MAGIC -- Row count validation
# MAGIC SELECT 'customers_raw' AS table_name, COUNT(*) AS row_count
# MAGIC FROM ops.bronze.customers_raw
# MAGIC UNION ALL
# MAGIC SELECT 'transactions_raw', COUNT(*)
# MAGIC FROM ops.bronze.transactions_raw
# MAGIC UNION ALL
# MAGIC SELECT 'accounts_raw', COUNT(*)
# MAGIC FROM ops.bronze.accounts_raw
# MAGIC UNION ALL
# MAGIC SELECT 'opportunities_raw', COUNT(*)
# MAGIC FROM ops.bronze.opportunities_raw
# MAGIC UNION ALL
# MAGIC SELECT 'leads_raw', COUNT(*)
# MAGIC FROM ops.bronze.leads_raw;