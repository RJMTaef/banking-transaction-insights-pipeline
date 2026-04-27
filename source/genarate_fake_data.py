# Goal
# generating fake banking data for customers, accounts, and transactions.
# 
import os
import random
from datetime import datetime, timedelta

import pandas as pd

random.seed(42)

RAW_DATA_PATH = "data/raw"

os.makedirs(RAW_DATA_PATH, exist_ok=True)

#customer data generation (not hardcoding customer data, making a system that generates random customers)
customer_names = [
    "Roslan Taef",
    "Amina Rahman",
    "Kris Potter",
    "Di Liu",
    "Jeff Machkintosh",
    "Kirsis Batistia",
    "Julio Romero",
    "Lungi Ngidi",
    "Robert Hernandez",
    "Sophie Roberts"
]

countries = ["England", "Bangladesh", "Canada", "USA", "India"]

risk_ratings = ["Standard", "Medium", "High"]

customers = []

# customer generation loop
for i in range(1,61):
    customer = {
        "customer_id": f"CUST{i:03d}",
        "name": random.choice(customer_names),
        "country": random.choice(countries),
        "signup_date": datetime(2021, 1, 1) + timedelta(days=random.randint(0, 1000)),
        "risk_rating": random.choice(risk_ratings)
    }

    customers.append(customer)

#converting the customer loop into table
customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    os.path.join(RAW_DATA_PATH, "customers.csv"),
    index=False
)

print("customers.csv created successfully")

#account setup
account_types = ["CHECKING", "SAVINGS", "CREDIT"]
account_statuses = ["ACTIVE", "CLOSED"]

accounts = []

for customer in customers:
    num_accounts = random.randint(1, 3)

    for _ in range(num_accounts):
        account = {
            "account_id": f"ACC{len(accounts)+1:04d}",
            "customer_id": customer["customer_id"],
            "account_type": random.choice(account_types),
            "open_date": customer["signup_date"] + timedelta(days=random.randint(0, 100)),
            "status": random.choice(account_statuses)
        }

        accounts.append(account)

accounts_df = pd.DataFrame(accounts)

accounts_df.to_csv(
    os.path.join(RAW_DATA_PATH, "accounts.csv"),
    index=False
)

print("accounts.csv created successfully")

transaction_types = ["DEBIT", "CREDIT"]
merchant_countries = ["Canada", "USA", "England", "India", "Bangladesh", "UAE", "Singapore"]

transactions = []

for account in accounts:
    num_transactions = random.randint(5, 25)

    for _ in range(num_transactions):
        transaction = {
            "transaction_id": f"TXN{len(transactions)+1:06d}",
            "account_id": account["account_id"],
            "transaction_date": account["open_date"] + timedelta(days=random.randint(0, 700)),
            "amount": round(random.uniform(10, 5000), 2),
            "transaction_type": random.choice(transaction_types),
            "merchant_country": random.choice(merchant_countries)
        }

        transactions.append(transaction)

# Duplicate records
duplicate_transactions = random.sample(transactions, 10)
transactions.extend(duplicate_transactions)

# Missing values
for transaction in random.sample(transactions, 10):
    transaction["merchant_country"] = None

# Large outliers
for transaction in random.sample(transactions, 8):
    transaction["amount"] = round(random.uniform(10000, 50000), 2)

# Negative invalid values
for transaction in random.sample(transactions, 5):
    transaction["amount"] = round(random.uniform(-5000, -10), 2)


transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    os.path.join(RAW_DATA_PATH, "transactions.csv"),
    index=False
)

print("transactions.csv created successfully")

# Output files:
# all in data folders, named as:
# customers.csv, accounts.csc, transactions.csv
# 
# Some data rules:
# -> All customers can have multiple accounts
# -> one customer can have multiple customers
# -> Some messy data will be added intentionally for cleaning practice.
#
#
# Steps:
# 1. Create customer records
# 2. Creat account records linked to customers
# 3. Create transactions records linked to accounts
# 4. Add intentional duplicates/missing values/ outliers.
# 5. Save all the datasets as CSV files.
#
#