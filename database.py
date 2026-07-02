import sqlite3

conn = sqlite3.connect("contracts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_name TEXT,
    risk_score INTEGER
)
""")

conn.commit()

print("Database Created Successfully")
