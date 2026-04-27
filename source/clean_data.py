import os
import pandas as pd

RAW_DATA_PATH = "data/raw"
CLEANED_DATA_PATH = "data/cleaned"

os.makedirs(CLEANED_DATA_PATH, exist_ok=True)

customers_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "customers.csv"))
accounts_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "accounts.csv"))
transactions_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "transactions.csv"))