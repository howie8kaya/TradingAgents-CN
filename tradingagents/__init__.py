"""TradingAgents-CN: AI-powered trading agents for Chinese and global markets.

A fork of hsliuping/TradingAgents-CN with enhanced support for Chinese financial
markets, data sources, and LLM providers.
"""

__version__ = "0.1.0"
__author__ = "TradingAgents-CN Contributors"
__description__ = "AI-powered multi-agent trading framework with Chinese market support"

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

__all__ = [
    "TradingAgentsGraph",
    "DEFAULT_CONFIG",
    "__version__",
]
