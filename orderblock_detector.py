class OrderblockDetector:
    def __init__(self, data, window=30):
        self.data = data
        self.window = window
        self.detected = self.detect()

    def detect(self):
        ob_zones = []
        for i in range(2, len(self.data) - self.window):
            c = self.data.iloc[i]
            prev = self.data.iloc[i - 1]
            next_block = self.data.iloc[i + 1: i + self.window]

            if c['close'] > c['open'] and prev['close'] > prev['open']:
                if next_block['close'].mean() < c['low']:
                    ob_zones.append({"type": "bearish", "index": i, "high": c['high'], "low": c['low']})
            if c['close'] < c['open'] and prev['close'] < prev['open']:
                if next_block['close'].mean() > c['high']:
                    ob_zones.append({"type": "bullish", "index": i, "high": c['high'], "low": c['low']})
        return ob_zones

    def as_confluence(self, entry):
        entry_price = entry.get("price")
        direction = entry.get("direction", "long")
        if not entry_price:
            return False
        relevant_obs = [ob for ob in self.detected if (
            (ob["type"] == "bullish" and direction == "long" and ob["low"] <= entry_price <= ob["high"]) or
            (ob["type"] == "bearish" and direction == "short" and ob["low"] <= entry_price <= ob["high"])
        )]
        return len(relevant_obs) > 0