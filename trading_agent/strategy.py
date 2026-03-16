from collections import deque

class MovingAverageStrategy:
    def __init__(self):
        self.prices = deque(maxlen=5)

    def evaluate(self, event):
        self.prices.append(event["price"])

        if len(self.prices) < 5:
            return None

        avg = sum(self.prices) / len(self.prices)

        if event["price"] > avg:
            return {
                "action": "BUY",
                "symbol": event["symbol"],
                "price": event["price"]
            }

        if event["price"] < avg:
            return {
                "action": "SELL",
                "symbol": event["symbol"],
                "price": event["price"]
            }

        return None