# binance_trade.py
from binance.client import Client

def extract_trade_data(api_key, api_secret, symbol, save_path):
    client = Client(api_key, api_secret)
    
    # Fetch recent trades for the specified trading pair
    trades = client.get_recent_trades(symbol=symbol)
    
    # Do something with the trade data (e.g., save to a file)
    with open(save_path, 'w') as file:
        file.write(str(trades))
    print("Trade data extracted successfully")
