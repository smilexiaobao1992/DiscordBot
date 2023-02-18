import sys
import requests
import pandas as pd
import logging


class CoinGeckoAPI:
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', stream=sys.stdout)

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3/"

    # 获取热门趋势代币
    @staticmethod
    def get_trending_coins():
        # Call API to get trending coins
        url = "https://api.coingecko.com/api/v3/search/trending"
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Failed to get trending coins: {response.text}")
            return None

        data = response.json()

        # Get BTC price
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Failed to get BTC price: {response.text}")
            return None

        btc_data = response.json()
        btc_price = float(btc_data['bitcoin']['usd'])

        # Convert data to DataFrame
        coins_data = []
        for item in data["coins"]:
            coin_data = item["item"]
            symbol = coin_data["symbol"]
            price_btc = coin_data["price_btc"]
            market_cap_rank = coin_data["market_cap_rank"]
            price_usd = price_btc * btc_price
            coins_data.append({"symbol": symbol, "market_cap_rank": market_cap_rank, "price_usd": price_usd})

        df = pd.DataFrame(coins_data)
        # Print output
        return df

    # 获取前100 1小时涨幅代币
    @staticmethod
    def get_trend_rank_coin():
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "price_change_percentage_1h_in_currency",
            "per_page": "100",
            "page": "1",
            "price_change_percentage": "1h,24h"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            sorted_data = sorted(data, key=lambda x: x['price_change_percentage_1h_in_currency'], reverse=True)
            df = pd.DataFrame(sorted_data[:20])
            return df
        else:
            print(f"Failed to get data from CoinGecko API: {response.text}")
