CREATE TABLE IF NOT EXISTS trades (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    action VARCHAR(10),
    price NUMERIC(10,2),
    timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS balance_history (
    id SERIAL PRIMARY KEY,
    balance NUMERIC(15,2),
    timestamp TIMESTAMP DEFAULT NOW()
);

INSERT INTO balance_history (balance) VALUES (100000.00);