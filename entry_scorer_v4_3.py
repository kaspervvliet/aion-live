from weighted_entry_scorer import WeightedEntryScorer
from contextual_confidence_modulator import ContextualConfidenceModulator

class EntryScorer:
    def __init__(self, bias):
        self.base_scorer = WeightedEntryScorer()
        self.conf_mod = ContextualConfidenceModulator(bias)

    def score_entries(self, entries):
        scored = []
        for entry in entries:
            base_score = self.base_scorer.score_entry(entry)
            mod_score = self.conf_mod.adjust(base_score, entry.get("confluences", []))
            entry["confidence_score"] = mod_score
            scored.append(entry)
        return scored