class ContextualConfidenceModulator:
    def __init__(self, bias):
        self.bias = bias

    def adjust(self, base_score, confluences):
        if self.bias == "range" and "MSSDetector" in confluences:
            return round(base_score - 0.2, 2)
        if self.bias == "bullish" and "OrderblockDetector" in confluences:
            return round(base_score + 0.1, 2)
        return base_score