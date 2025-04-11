from dynamic_strategy_morpher import DynamicStrategyMorpher
from strategy_switcher import StrategySwitcher
import json

def adapt_config_with_morphing(config, bias):
    switcher = StrategySwitcher(config)
    config = switcher.adapt_strategy_to_bias(bias)
    morpher = DynamicStrategyMorpher(bias)
    return morpher.morph(config)