
import time
from data import get_latest_data
from strategy_config_loader import load_config
from strategy_manager import StrategyManager
from entry_scorer import EntryScorer
from gpt_validator import GPTValidator
from telegram_notifier import TelegramNotifier

class LiveMarketScanner:
    def __init__(self, assets, interval_sec=60, config_path="strategy_config.json"):
        self.assets = assets
        self.interval = interval_sec
        self.config_path = config_path

    def scan_loop(self):
        print(f"🟢 Live scanner gestart voor {len(self.assets)} assets, elke {self.interval} sec.")
        while True:
            for symbol in self.assets:
    print("Live markt scanning gestart.")
🔍 Scannen: {symbol}")
                data = get_latest_data(symbol)
                strategy, config = load_config(self.config_path, data)

                manager = StrategyManager(data, strategy_name=config["strategy_name"])
                entries, performance = manager.run()

                if entries:
                    scorer = EntryScorer()
                    scored = scorer.score_entries(entries)
                    validator = GPTValidator()
                    explained = validator.explain_all(scored)
                    high_conf = [e for e in explained if e["confidence_score"] >= config["settings"]["confidence_threshold"]]

                    if high_conf:
                        print(f"📢 {symbol} → {len(high_conf)} high-confidence entries gevonden!")
                        for entry in high_conf:
                            print("→", entry["gpt_explanation"])
                    else:
                        print("⚪ Geen sterke setups bij deze scan.")
                else:
                    print("⚪ Geen entries gedetecteerd.")

            print(f"
⏱️ Wacht {self.interval} seconden voor volgende scan...")
            time.sleep(self.interval)
