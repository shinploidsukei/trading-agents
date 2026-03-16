import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="trading",
        user="trader",
        password="trader",
        host="postgres",
        port=5432
    )

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id SERIAL PRIMARY KEY,
            symbol VARCHAR(10),
            action VARCHAR(10),
            price NUMERIC,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()