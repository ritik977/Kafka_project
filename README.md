# Kafka Transaction Processing Pipeline

## Overview
This project simulates a real-time transaction processing system using Kafka.

## Components
- **Producer:** Generates and sends transaction data to a Kafka topic.
- **Consumer:** Reads and processes transaction data, storing results in SQLite.
- **Dashboard (Optional):** Simple console output for monitoring.

## Setup and Running
1. Install Kafka and Python dependencies.
2. Start Kafka server.
3. Run the producer: `python producer.py`
4. Run the consumer: `python consumer.py`
5. (Optional) Run the monitoring script for insights.

## Architecture
- The producer sends randomly generated transaction data to a Kafka topic.
- The consumer processes each transaction and stores it in an SQLite database.

## Assumptions
- Transactions are simple JSON objects with fields like `transaction_id`, `timestamp`, `amount`, `currency`, and `status`.

## Fault Tolerance
- The producer retries on failures.
- The consumer handles message duplication.
