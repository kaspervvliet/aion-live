class RiskUnitAllocator:
    def __init__(self, account_size, risk_pct=0.02, leverage=10):
        self.account_size = account_size
        self.risk_pct = risk_pct
        self.leverage = leverage

    def calculate_position_size(self, sl_percent):
        risk = self.account_size * self.risk_pct
        raw_position = risk / (sl_percent / 100)
        return round(raw_position * self.leverage, 2)