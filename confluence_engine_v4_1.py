from orderblock_detector import OrderblockDetector
from eqh_eql_detector import EQH_EQLDetector
from mss_detector import MSSDetector

class ConfluenceEngineV4:
    def __init__(self, data, config=None):
        self.data = data
        self.config = config or {}
        self.modules = self.load_modules()

    def load_modules(self):
        modules = []
        if self.config.get("orderblock", True):
            modules.append(OrderblockDetector(self.data))
        if self.config.get("eq_levels", True):
            modules.append(EQH_EQLDetector(self.data))
        if self.config.get("mss", True):
            modules.append(MSSDetector(self.data))
        return modules

    def evaluate_entry(self, entry):
        result = []
        for module in self.modules:
            if module.as_confluence(entry):
                result.append(module.__class__.__name__)
        return result