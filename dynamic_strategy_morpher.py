class DynamicStrategyMorpher:
    def __init__(self, bias):
        self.bias = bias

    def morph(self, config):
        if self.bias == "bullish":
            config["confluences"] = [{"type": "OrderblockDetector"}, {"type": "MSSDetector"}]
        elif self.bias == "bearish":
            config["confluences"] = [{"type": "EQH_EQLDetector"}, {"type": "MSSDetector"}]
        elif self.bias == "range":
            config["confluences"] = [{"type": "EQH_EQLDetector"}]
        return config