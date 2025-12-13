import time
import yfinance as yf
from langchain.tools import tool
from MarketInsight.utils.logger import get_logger

logger = get_logger("tools.py")

# --------------------------------------------------------------------------------
# Tool 1: Retrieve Company Stock Price
# --------------------------------------------------------------------------------
@tool('get_stock_price', description="A function that returns the current stock price of a given ticker")
def get_stock_price(ticker: str):
    logger.info(f"Retrieving Stock Price of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    stock_price = stock.info['regularMarketPrice']
    end_time = time.time()
    logger.info(f"Retrieved Stock Price of {ticker} in {end_time - start_time:.3f} seconds")
    return stock_price

# --------------------------------------------------------------------------------
# Tool 2: Retrieve Company Stock Historical Data
# --------------------------------------------------------------------------------
@tool('get_historical_data', description="A function that returns the historical data of a given ticker in the given start and end date")
def get_historical_data(ticker: str, start_date: str, end_date: str):
    logger.info(f"Retrieving Historical Data of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    historical_data = stock.history(start=start_date, end=end_date).to_dict()
    end_time = time.time()
    logger.info(f"Retrieved Historical Data of {ticker} in {end_time - start_time:.3f} seconds")
    return historical_data

# --------------------------------------------------------------------------------
# Tool 3: Retrieve Company Stock News
# --------------------------------------------------------------------------------
@tool('get_stock_news', description="A function that returns the news of a given ticker")
def get_stock_news(ticker: str):
    logger.info(f"Retrieving News of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    news = stock.news
    end_time = time.time()
    logger.info(f"Retrieved News of {ticker} in {end_time - start_time:.3f} seconds")
    return news

# --------------------------------------------------------------------------------
# Tool 4: Retrieve Company's Balance Sheet
# --------------------------------------------------------------------------------
@tool('get_balance_sheet', description="A function that returns the balance sheet of a given ticker")
def get_balance_sheet(ticker: str):
    logger.info(f"Retrieving Balance Sheet of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    balance_sheet = stock.balance_sheet.to_dict()
    end_time = time.time()
    logger.info(f"Retrieved Balance Sheet of {ticker} in {end_time - start_time:.3f} seconds")
    return balance_sheet

# --------------------------------------------------------------------------------
# Tool 5: Retrieve Company's Income Statement
# --------------------------------------------------------------------------------
@tool('get_income_statement', description="A function that returns the income statement of a given ticker")
def get_income_statement(ticker: str):
    logger.info(f"Retrieving Income Statement of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    income_statement = stock.financials.to_dict()
    logger.info(f"Retrieved Income Statement of {ticker} in {time.time() - start_time:.3f} seconds")
    return income_statement

# --------------------------------------------------------------------------------
# Tool 6: Retrieve Company's Cash Flow Statement
# --------------------------------------------------------------------------------
@tool('get_cash_flow', description="A function that returns the cash flow statement of a given ticker")
def get_cash_flow(ticker: str):
    logger.info(f"Retrieving Cash Flow of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow.to_dict()
    logger.info(f"Retrieved Cash Flow of {ticker} in {time.time() - start_time:.3f} seconds")
    return cash_flow

# --------------------------------------------------------------------------------
# Tool 7: Retrieve Company Info & Ratios
# --------------------------------------------------------------------------------
@tool('get_company_info', description="A function that returns company profile and key financial ratios")
def get_company_info(ticker: str):
    logger.info(f"Retrieving Company Info of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    info = stock.info
    logger.info(f"Retrieved Company Info of {ticker} in {time.time() - start_time:.3f} seconds")
    return info

# --------------------------------------------------------------------------------
# Tool 8: Retrieve Dividend History
# --------------------------------------------------------------------------------
@tool('get_dividends', description="A function that returns the dividend payment history of a given ticker")
def get_dividends(ticker: str):
    logger.info(f"Retrieving Dividends of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    dividends = stock.dividends.to_dict()
    logger.info(f"Retrieved Dividends of {ticker} in {time.time() - start_time:.3f} seconds")
    return dividends

# --------------------------------------------------------------------------------
# Tool 9: Retrieve Stock Split History
# --------------------------------------------------------------------------------
@tool('get_splits', description="A function that returns the stock split history of a given ticker")
def get_splits(ticker: str):
    logger.info(f"Retrieving Stock Splits of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    splits = stock.splits.to_dict()
    logger.info(f"Retrieved Stock Splits of {ticker} in {time.time() - start_time:.3f} seconds")
    return splits


# --------------------------------------------------------------------------------
# Tool 10: Retrieve Institutional Holders
# --------------------------------------------------------------------------------
@tool('get_institutional_holders', description="A function that returns the institutional ownership data of a given ticker")
def get_institutional_holders(ticker: str):
    logger.info(f"Retrieving Institutional Holders of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    holders = stock.institutional_holders.to_dict()
    logger.info(f"Retrieved Institutional Holders of {ticker} in {time.time() - start_time:.3f} seconds")
    return holders

# --------------------------------------------------------------------------------
# Tool 11: Retrieve Major Share Holders
# --------------------------------------------------------------------------------
@tool('get_major_shareholders', description="A function that returns the major share holder data of a given ticker")
def get_major_shareholders(ticker: str):
    logger.info(f"Retrieving Major Share Holders of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    holders = stock.major_holders.to_dict()
    logger.info(f"Retrieved Major Share Holders of {ticker} in {time.time() - start_time:.3f} seconds")
    return holders

# --------------------------------------------------------------------------------
# Tool 12: Retrieve Mutual Fund Holders
# --------------------------------------------------------------------------------
@tool('get_mutual_fund_holders', description="A function that returns the mutual fund ownership data of a given ticker")
def get_mutual_fund_holders(ticker: str):
    logger.info(f"Retrieving Mutual Fund Holders of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    holders = stock.mutualfund_holders.to_dict()
    logger.info(f"Retrieved Mutual Fund Holders of {ticker} in {time.time() - start_time:.3f} seconds")
    return holders

# --------------------------------------------------------------------------------
# Tool 13: Retrieve Insider Transactions
# --------------------------------------------------------------------------------
@tool('get_insider_transactions', description="A function that returns the insider buy/sell transactions of a given ticker")
def get_insider_transactions(ticker: str):
    logger.info(f"Retrieving Insider Transactions of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    insider_txn = stock.insider_transactions.to_dict()
    logger.info(f"Retrieved Insider Transactions of {ticker} in {time.time() - start_time:.3f} seconds")
    return insider_txn

# --------------------------------------------------------------------------------
# Tool 14: Retrieve Analyst Recommendations
# --------------------------------------------------------------------------------
@tool('get_analyst_recommendations', description="A function that returns the analyst recommendations of a given ticker")
def get_analyst_recommendations(ticker: str):
    logger.info(f"Retrieving Analyst Recommendations of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations.to_dict()
    logger.info(f"Retrieved Analyst Recommendations of {ticker} in {time.time() - start_time:.3f} seconds")
    return recommendations

# --------------------------------------------------------------------------------
# Tool 15: Retrieve Analyst Recommendations Summary
# --------------------------------------------------------------------------------
@tool('get_analyst_recommendations_summary', description="A function that returns the analyst recommendations summary of a given ticker")
def get_analyst_recommendations_summary(ticker: str):
    logger.info(f"Retrieving Analyst Recommendations Summary of {ticker}")
    start_time = time.time()
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations_summary.to_dict()
    logger.info(f"Retrieved Analyst Recommendations Summary of {ticker} in {time.time() - start_time:.3f} seconds")
    return recommendations