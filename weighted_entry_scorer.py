class WeightedEntryScorer:
    def __init__(self, weights=None):
        self.weights = weights or {
            "OrderblockDetector": 1.0,
            "EQH_EQLDetector": 0.8,
            "MSSDetector": 0.6
        }

    def score_entry(self, entry):
        active = entry.get("confluences", [])
        score = sum([self.weights.get(c, 0.5) for c in active])
        return round(score / len(self.weights), 2) if active else 0.0