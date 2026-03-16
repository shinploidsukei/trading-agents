import time
from db import get_connection, create_tables

create_tables()
conn = get_connection()
cur = conn.cursor()

while True:
    cur.execute("SELECT * FROM trades ORDER BY timestamp DESC LIMIT 5")
    rows = cur.fetchall()
    for row in rows:
        print(f"Trade: {row}")
    time.sleep(5)