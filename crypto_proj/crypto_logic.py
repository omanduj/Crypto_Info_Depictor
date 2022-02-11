import requests
import json


class CoinInfo:
    """Purpose: To create an object to hold all info on coins
    Parameters: None
    Return Value: None
    """

    def __init__(self, name):
        self.symbol = None
        self.exchanger_name = None
        self.name = name
        self.purchase = None
        self.sell = None


def create_url_coinbase(symbol, action):
    """Purpose: To create the required URL to get info from coinbase
    Parameters: symbol = The symbol of the coin, action = whether you are buying or selling a coin
    Return Value: The purchase and sell price for a given coin
    """
    response = requests.request(
        "Get", "https://api.coinbase.com/v2/prices/{}/{}".format(symbol, action)
    )
    return response.json()["data"]["amount"]


def create_url_blockchain(symbol):
    """Purpose: To create the required URL to get info from blockchain
    Parameters: symbol = The symbol of the coin
    Return Value: The purchase and sell price for a given coin
    """
    response = requests.request(
        "Get", "https://api.blockchain.com/v3/exchange/tickers/{}".format(symbol)
    )
    return (response.json()["price_24h"], response.json()["last_trade_price"])


def coinbase(coin_name_dict):
    """Purpose: To obtain selling and purchase price of inputted coins on coinbase
    Parameters: coin_symbols = A list of symbols representing the coin
                 coin_names = A list containing names of the coins
    Return Value: dict_of_coins = A dictionary whos keys are the names of the inputted coins
                 and values are CoinInfo objects containing name, symbol, sell, and purchase price
    """
    dict_of_coins = {}

    for coin in coin_name_dict:
        dict_of_coins[coin] = CoinInfo(coin)
        dict_of_coins[coin].symbol = coin_name_dict[coin]
        dict_of_coins[coin].exchanger_name = "Coinbase"
        dict_of_coins[coin].sell = create_url_coinbase(coin_name_dict[coin], "sell")
        dict_of_coins[coin].purchase = create_url_coinbase(coin_name_dict[coin], "buy")

    return dict_of_coins


def blockchain(coin_name_dict):
    """Purpose: To obtain selling and purchase price of inputted coins on blockchain
    Parameters: coin_symbols = A list of symbols representing the coin
                 coin_names = A list containing names of the coins
    Return Value: dict_of_coins = A dictionary whos keys are the names of the inputted coins
                 and values are CoinInfo objects containing name, symbol, sell, and purchase price
    """
    dict_of_coins = {}

    for coin in coin_name_dict:
        dict_of_coins[coin] = CoinInfo(coin)
        dict_of_coins[coin].symbol = coin_name_dict[coin]
        dict_of_coins[coin].exchanger_name = "Blockchain"
        dict_of_coins[coin].purchase, dict_of_coins[coin].sell = create_url_blockchain(
            coin_name_dict[coin]
        )

    return dict_of_coins


def find_best(coin_name_dict):
    """Purpose: To identify the best location to purchase and sell a given coin
    Parameters: coin_symbols = A list of symbols representing the coin
                coin_names = A list containing names of the coins
    Return Value: dict_of_locations = A dictionary containing names of companies as keys, whose values
                         are company name and X price
    Note: If adding a new exchanger, make sure to edit for loop to contian new dictionary's coins
    """
    dict_of_coins_blockchain = blockchain(coin_name_dict)
    dict_of_coins_coinbase = coinbase(coin_name_dict)
    dict_of_locations = {"best_buy": {}, "best_sell": {}}

    for coin in dict_of_coins_blockchain.keys():
        if float(dict_of_coins_blockchain[coin].purchase) == min(
            float(dict_of_coins_blockchain[coin].purchase),
            float(dict_of_coins_coinbase[coin].purchase),
        ):
            dict_of_locations["best_buy"][dict_of_coins_blockchain[coin].name] = {
                "company": dict_of_coins_blockchain[coin].exchanger_name,
                "purchase": dict_of_coins_blockchain[coin].purchase,
            }

        if float(dict_of_coins_coinbase[coin].purchase) == min(
            float(dict_of_coins_blockchain[coin].purchase),
            float(dict_of_coins_coinbase[coin].purchase),
        ):
            dict_of_locations["best_buy"][dict_of_coins_blockchain[coin].name] = {
                "company": dict_of_coins_blockchain[coin].exchanger_name,
                "purchase": dict_of_coins_blockchain[coin].purchase,
            }

        if float(dict_of_coins_blockchain[coin].sell) == max(
            float(dict_of_coins_blockchain[coin].sell),
            float(dict_of_coins_coinbase[coin].sell),
        ):
            dict_of_locations["best_sell"][dict_of_coins_blockchain[coin].name] = {
                "company": dict_of_coins_blockchain[coin].exchanger_name,
                "purchase": dict_of_coins_blockchain[coin].sell,
            }

        if float(dict_of_coins_coinbase[coin].sell) == max(
            float(dict_of_coins_blockchain[coin].sell),
            float(dict_of_coins_coinbase[coin].sell),
        ):
            dict_of_locations["best_sell"][dict_of_coins_coinbase[coin].name] = {
                "company": dict_of_coins_coinbase[coin].exchanger_name,
                "purchase": dict_of_coins_coinbase[coin].sell,
            }

    return dict_of_locations
find_best({"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD", "Dogecoin": "DOGE-USD"})
