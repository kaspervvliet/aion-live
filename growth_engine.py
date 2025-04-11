class GrowthEngine:
    def __init__(self, starting_equity):
        self.equity = starting_equity
        self.history = []

    def update_equity(self, trade_result):
        self.equity += trade_result
        self.history.append(self.equity)

    def get_equity(self):
        return round(self.equity, 2)

    def get_growth_rate(self):
        if len(self.history) < 2:
            return 0.0
        return round((self.history[-1] - self.history[0]) / self.history[0] * 100, 2)