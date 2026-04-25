import sqlite3

DB_PATH = "crypto.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_name TEXT,
            price FLOAT,
            change_24h FLOAT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def load_data(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for item in data:
        cursor.execute("""
            INSERT INTO crypto_prices (coin_name, price, change_24h, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            item["coin_name"],
            item["price"],
            item["change_24h"],
            item["timestamp"]
        ))

    conn.commit()
    conn.close()