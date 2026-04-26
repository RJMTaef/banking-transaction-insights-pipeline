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