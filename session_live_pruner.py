class SessionLivePruner:
    def __init__(self):
        self.fail_count = {}

    def update(self, entry_type, result):
        if entry_type not in self.fail_count:
            self.fail_count[entry_type] = 0
        if result == "loss":
            self.fail_count[entry_type] += 1

    def is_disabled(self, entry_type):
        return self.fail_count.get(entry_type, 0) >= 2