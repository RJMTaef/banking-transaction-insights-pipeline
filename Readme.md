# Banking Transaction Insights Pipeline

## Overview

This project simulates a banking transaction data pipeline. Fake customer, account, and transaction data is generated, cleaned, loaded into a SQLite database, and analyzed using SQL queries.

The goal is to demonstrate practical skills in:

- Python
- Pandas
- SQL
- SQLite
- Data cleaning
- Data modeling
- Data analysis
- Data visualization

---

## Project Structure

```text
banking-transaction-insights-pipeline/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── src/
│   ├── generate_fake_data.py
│   ├── clean_data.py
│   ├── load_to_db.py
│   └── analyze.py
│
├── visuals/
│
├── README.md
├── requirements.txt
└── .gitignore
