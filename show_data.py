import sqlite3

conn = sqlite3.connect("contracts.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM contracts")

rows = cursor.fetchall()

for row in rows:
    print(row)
