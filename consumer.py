from kafka import KafkaConsumer
import json
import sqlite3

# Connecting to SQLite database (or creating it if it doesn't exist)
conn = sqlite3.connect('transactions.db')
c = conn.cursor()

# Ensuring the table structure exists
c.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id TEXT,
        timestamp TEXT,
        amount REAL,
        currency TEXT,
        status TEXT
    )
''')
conn.commit()

# Setting up the Kafka consumer
consumer = KafkaConsumer('transactions',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

def process_transaction(transaction):
    # Placeholder for any processing logic; currently just returns the transaction as-is
    return transaction

def store_transaction(transaction):
    # Inserting the processed transaction into the database
    c.execute('''
        INSERT INTO transactions (transaction_id, timestamp, amount, currency, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (transaction['transaction_id'], transaction['timestamp'], transaction['amount'],
          transaction['currency'], transaction['status']))
    conn.commit()

if __name__ == "__main__":
    for message in consumer:
        transaction = process_transaction(message.value)
        store_transaction(transaction)  # Storing the transaction in SQLite
        print(f"Processed and stored: {transaction}")  # Visibility into the process
