class DrawdownMonitor:
    def __init__(self, max_drawdown_pct=0.2):
        self.max_drawdown_pct = max_drawdown_pct
        self.peak = 0
        self.current = 0
        self.alert = False

    def update(self, equity):
        if equity > self.peak:
            self.peak = equity
        self.current = equity
        drawdown = (self.peak - equity) / self.peak if self.peak > 0 else 0
        self.alert = drawdown >= self.max_drawdown_pct
        return self.alert