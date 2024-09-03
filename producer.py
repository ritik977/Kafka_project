from kafka import KafkaProducer
import json
import time
import uuid
from datetime import datetime
import random

# Setting up the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_transaction():
    # Generates a simple transaction with a few random values
    return {
        'transaction_id': str(uuid.uuid4()),  # Unique transaction ID
        'timestamp': datetime.now().isoformat(),  # Current timestamp
        'amount': round(random.uniform(10, 1000), 2),  # Random transaction amount
        'currency': random.choice(['USD', 'EUR', 'GBP']),  # Random currency
        'status': random.choice(['pending', 'completed', 'failed'])  # Random status
    }

def produce_transactions():
    while True:
        transaction = generate_transaction()
        producer.send('transactions', transaction)  # Sending the transaction to Kafka topic
        print(f"Sent: {transaction}")  # Simple print statement for visibility
        time.sleep(1)  # Sleep for a second to control the transaction generation rate

if __name__ == "__main__":
    produce_transactions()  # Start producing transactions
