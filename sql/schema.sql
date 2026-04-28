CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    country TEXT,
    signup_date TEXT,   
    risk_rating TEXT
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT PRIMARY KEY,
    customer_id TEXT,
    account_type TEXT,
    open_date TEXT,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    account_id TEXT,
    transaction_date TEXT,
    amount REAL,
    transaction_type TEXT,
    merchant_country TEXT,
    is_large_transaction INTEGER,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);