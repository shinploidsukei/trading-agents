from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

symbols = ['AAPL', 'GOOG', 'TSLA', 'AMZN']

while True:
    event = {
        'symbol': random.choice(symbols),
        'price': round(random.uniform(100, 250), 2)
    }
    producer.send('market_events', event)
    print(f"Produced event: {event}")
    time.sleep(1)