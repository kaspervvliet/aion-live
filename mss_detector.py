class MSSDetector:
    def __init__(self, data):
        self.data = data
        self.shifts = self.detect_mss()

    def detect_mss(self):
        shifts = []
        for i in range(2, len(self.data)):
            low_1 = self.data["low"].iloc[i - 2]
            low_2 = self.data["low"].iloc[i - 1]
            high_1 = self.data["high"].iloc[i - 2]
            high_2 = self.data["high"].iloc[i - 1]
            close = self.data["close"].iloc[i]

            if low_2 < low_1 and close > high_1:
                shifts.append({"type": "bullish", "index": i, "price": close})
            if high_2 > high_1 and close < low_1:
                shifts.append({"type": "bearish", "index": i, "price": close})
        return shifts

    def as_confluence(self, entry):
        direction = entry.get("direction", "long")
        price = entry.get("price")
        if not price:
            return False
        relevant = [m for m in self.shifts if (
            m["type"] == "bullish" and direction == "long" and abs(m["price"] - price) / price < 0.01 or
            m["type"] == "bearish" and direction == "short" and abs(m["price"] - price) / price < 0.01
        )]
        return len(relevant) > 0