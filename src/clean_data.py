import os
import pandas as pd

RAW_DATA_PATH = "data/raw"
CLEANED_DATA_PATH = "data/cleaned"

os.makedirs(CLEANED_DATA_PATH, exist_ok=True)

customers_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "customers.csv"))
accounts_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "accounts.csv"))
transactions_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "transactions.csv"))

#track original row counts
original_transaction_count = len(transactions_df)

#remove exact duplicate transaction rows
transactions_df = transactions_df.drop_duplicates()

duplicates_removed = original_transaction_count - len(transactions_df)

print(f"Duplicate transactions removed: {duplicates_removed}")

# Track missing values before cleaning
missing_before = transactions_df["merchant_country"].isna().sum()

#fill missing merchant_country with "UNKNOWN"
transactions_df["merchant_country"] = transactions_df["merchant_country"].fillna("UNKNOWN")

#track after
missing_after = transactions_df["merchant_country"].isna().sum()

print(f"Missing merchant_country before: {missing_before}, after: {missing_after}")

#remove negative ammounts
negative_amount_count = (transactions_df["amount"] < 0).sum()

transactions_df = transactions_df[transactions_df["amount"] >= 0]

print(f"Negative amount transactions removed: {negative_amount_count}")

# Flag unusually large transactions
transactions_df["is_large_transaction"] = transactions_df["amount"] > 10000

large_transaction_count = transactions_df["is_large_transaction"].sum()

print(f"Large transactions flagged: {large_transaction_count}")

customers_df.to_csv(
    os.path.join(CLEANED_DATA_PATH, "customers_cleaned.csv"),
    index=False
)

accounts_df.to_csv(
    os.path.join(CLEANED_DATA_PATH, "accounts_cleaned.csv"),
    index=False
)

transactions_df.to_csv(
    os.path.join(CLEANED_DATA_PATH, "transactions_cleaned.csv"),
    index=False
)

print("Cleaned CSV files saved successfully")