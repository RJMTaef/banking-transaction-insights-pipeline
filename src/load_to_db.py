import os
import sqlite3
import pandas as pd

CLEANED_DATA_PATH = "data/cleaned"
DATABASE_PATH = "banking_transactions.db"
SCHEMA_PATH = "sql/schema.sql"

customers_df = pd.read_csv(os.path.join(CLEANED_DATA_PATH, "customers_cleaned.csv"))
accounts_df = pd.read_csv(os.path.join(CLEANED_DATA_PATH, "accounts_cleaned.csv"))
transactions_df = pd.read_csv(os.path.join(CLEANED_DATA_PATH, "transactions_cleaned.csv"))

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

#Load schema and create tables
with open(SCHEMA_PATH, "r") as f:
    schema_sql = f.read()

cursor.executescript(schema_sql)

print("Database and tables ready")

#cleaning database
customers_df.to_sql("customers", conn, if_exists="replace", index=False)
accounts_df.to_sql("accounts", conn, if_exists="replace", index=False)
transactions_df.to_sql("transactions", conn, if_exists="replace", index=False)

conn.commit()

print("Cleaned data loaded into database successfully")

