import time
from db import get_connection, create_tables

create_tables()

symbols = ['AAPL', 'TSLA', 'GOOG', 'MSFT']

while True:
    conn = get_connection()
    cur = conn.cursor()
    symbol = symbols[int(time.time()) % len(symbols)]
    price = round(100 + (time.time() % 50), 2)
    action = 'BUY' if int(time.time()) % 2 == 0 else 'SELL'
    cur.execute(
        "INSERT INTO trades (symbol, action, price) VALUES (%s, %s, %s)",
        (symbol, action, price)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted trade: {action} {symbol} at {price}")
    time.sleep(5)