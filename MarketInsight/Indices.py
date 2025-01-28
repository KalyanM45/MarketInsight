from nsepython import index_history
from MongoDB_Utils import Push_Records, Get_Records

def push_to_mongodb():
    symbol = "NIFTY 50"
    start_date = "22-Apr-1996"
    end_date = "25-Jan-2025"
    data = index_history(symbol, start_date, end_date)
    data.rename(columns={"HistoricalDate": "Date", "OPEN": "Open", "HIGH": "High", "LOW": "Low", "CLOSE": "Close"}, inplace=True)
    data = data[["Date", "Open", "High", "Low", "Close"]]
    records = data.to_dict(orient='records')
    Push_Records(records, f"{symbol}")


    

if __name__ == "__main__":
    push_to_mongodb()
