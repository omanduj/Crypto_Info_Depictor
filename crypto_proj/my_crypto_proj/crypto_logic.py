import requests
import json

class CoinInfo():
    """Purpose: To crease an object to hold all info on coins
        Parameters: None
        Return Value: None
    """
    def __init__(self, name): #Do I need name attribute here?
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
    response = requests.request('Get', 'https://api.coinbase.com/v2/prices/{}/{}'.format(symbol, action))
    return response.json()['data']['amount']

def create_url_blockchain(symbol):
    """Purpose: To create the required URL to get info from blockchain
        Parameters: symbol = The symbol of the coin
        Return Value: The purchase and sell price for a given coin
    """
    response = requests.request('Get', 'https://api.blockchain.com/v3/exchange/tickers/{}'.format(symbol))
    return (response.json()['price_24h'], response.json()['last_trade_price'])

def coinbase():
    """Purpose: To obtain selling and purchase price of inputted coins on coinbase
        Parameters: None
        Return Value: dict_of_coins = A dictionary whos keys are the names of the inputted coins
                    and values are CoinInfo objects containing name, symbol, sell, and purchase price
    """
    coin_symbols = ['BTC-USD', 'ETH-USD', 'DOGE-USD']
    coin_names = ['Bitcoin', 'Etherium', 'Dogecoin']
    dict_of_coins = {}

    for coin in range(len(coin_names)):
        dict_of_coins[coin_names[coin]] = CoinInfo(coin_names[coin])
        dict_of_coins[coin_names[coin]].symbol = coin_symbols[coin]
        dict_of_coins[coin_names[coin]].exchanger_name = 'Coinbase'
        dict_of_coins[coin_names[coin]].sell = create_url_coinbase(coin_symbols[coin], 'sell')
        dict_of_coins[coin_names[coin]].purchase = create_url_coinbase(coin_symbols[coin], 'buy')

    return(dict_of_coins)


def blockchain():
    """Purpose: To obtain selling and purchase price of inputted coins on blockchain
        Parameters: None
        Return Value: dict_of_coins = A dictionary whos keys are the names of the inputted coins
                    and values are CoinInfo objects containing name, symbol, sell, and purchase price
    """
    coin_symbols = ['BTC-USD', 'ETH-USD', 'DOGE-USD']
    coin_names = ['Bitcoin', 'Etherium', 'Dogecoin']
    dict_of_coins = {}

    for coin in range(len(coin_symbols)):
        dict_of_coins[coin_names[coin]] = CoinInfo(coin_names[coin])
        dict_of_coins[coin_names[coin]].symbol = coin_symbols[coin]
        dict_of_coins[coin_names[coin]].exchanger_name = 'Blockchain'
        dict_of_coins[coin_names[coin]].sell, dict_of_coins[coin_names[coin]].purchase = create_url_blockchain(coin_symbols[coin])

    return(dict_of_coins)
blockchain()


def find_best():
    """Purpose: To identify the best location to purchase and sell a given coin
       Parameters: None
       Return Value: best_buy = A list of the best locations to buy each respective coin,
                     best_sell = A list of the best locations to sell each respective coin

       Note: If adding a new exchanger, make sure to edit for loop to contian new dictionary's coins
    """
    dict_of_coins_blockchain = blockchain()
    dict_of_coins_coinbase = coinbase()

    best_buy = []
    best_sell = []

    for i in dict_of_coins_blockchain.keys():
        if float(dict_of_coins_blockchain[i].purchase) == min(float(dict_of_coins_blockchain[i].purchase), float(dict_of_coins_coinbase[i].purchase)):
            best_buy.append((dict_of_coins_blockchain[i].name, dict_of_coins_blockchain[i].exchanger_name, dict_of_coins_blockchain[i].purchase))

        if float(dict_of_coins_coinbase[i].purchase) == min(float(dict_of_coins_blockchain[i].purchase), float(dict_of_coins_coinbase[i].purchase)):
            best_buy.append((dict_of_coins_coinbase[i].name, dict_of_coins_coinbase[i].exchanger_name, dict_of_coins_coinbase[i].purchase))

        if float(dict_of_coins_blockchain[i].sell) == max(float(dict_of_coins_blockchain[i].sell), float(dict_of_coins_coinbase[i].sell)):
            best_sell.append((dict_of_coins_blockchain[i].name, dict_of_coins_blockchain[i].exchanger_name, dict_of_coins_blockchain[i].sell))

        if float(dict_of_coins_coinbase[i].sell) == max(float(dict_of_coins_blockchain[i].sell), float(dict_of_coins_coinbase[i].sell)):
            best_sell.append((dict_of_coins_coinbase[i].name, dict_of_coins_coinbase[i].exchanger_name, dict_of_coins_coinbase[i].sell))

    return (best_buy, best_sell)

find_best()
