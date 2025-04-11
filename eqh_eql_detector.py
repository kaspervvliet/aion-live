class EQH_EQLDetector:
    def __init__(self, data, threshold=0.05):
        self.data = data
        self.threshold = threshold
        self.eq_highs = self.find_equal_levels(kind="high")
        self.eq_lows = self.find_equal_levels(kind="low")

    def find_equal_levels(self, kind="high"):
        levels = []
        source = self.data[kind]
        for i in range(2, len(source)):
            a, b = source[i - 2], source[i - 1]
            if abs(a - b) / max(a, b) < self.threshold:
                levels.append(round((a + b) / 2, 2))
        return list(set(levels))

    def as_confluence(self, entry):
        price = entry.get("price")
        if not price:
            return False
        direction = entry.get("direction", "long")
        if direction == "long":
            return any(abs(price - lvl) / lvl < self.threshold for lvl in self.eq_lows)
        elif direction == "short":
            return any(abs(price - lvl) / lvl < self.threshold for lvl in self.eq_highs)
        return False