from session_live_pruner import SessionLivePruner

class StrategyManager:
    def __init__(self, data, strategy_name="ModularStrategy"):
        self.data = data
        self.strategy_name = strategy_name
        self.pruner = SessionLivePruner()

    def run(self, strategy):
        entries = strategy.find_entries()
        filtered = []

        for entry in entries:
            for c in entry.get("confluences", []):
                if not self.pruner.is_disabled(c):
                    filtered.append(entry)
                    break
        return filtered