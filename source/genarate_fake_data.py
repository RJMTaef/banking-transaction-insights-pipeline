# Goal
# generating fake banking data for customers, accounts, and transactions.
# 
import os
import random
from datetime import datetime, timedelta


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