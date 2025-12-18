import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from MarketInsight.utils.tools import *
from MarketInsight.utils.logger import get_logger
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

load_dotenv()
logger = get_logger(__name__)

model = ChatOpenAI(
        model = "c1/openai/gpt-5/v-20250930",
        base_url = "https://api.thesys.dev/v1/embed/"
    )

agent = create_agent(
    model,
    tools = [get_stock_price, get_historical_data, get_stock_news, get_balance_sheet, get_income_statement, get_cash_flow,
            get_company_info, get_dividends, get_splits, get_institutional_holders, get_major_shareholders,
            get_mutual_fund_holders, get_insider_transactions, get_analyst_recommendations, get_analyst_recommendations_summary, get_ticker],
    checkpointer = MemorySaver()
)

logger.info("Agent Initiated Successfully")