import requests
import json

class CoinInfo():
    """Purpose: To crease an object to hold all info on coins
        Parameters: None
        Return Value: None
    """
    def __init__(self, name):
        self.symbol = None
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
    coin_symbols = ['BTC-USD', 'ETH-USD']
    coin_names = ['Bitcoin', 'Etherium']
    dict_of_coins = {}

    for coin in range(len(coin_names)):
        dict_of_coins[coin_names[coin]] = CoinInfo(coin_names[coin])
        dict_of_coins[coin_names[coin]].symbol = coin_symbols[coin]
        dict_of_coins[coin_names[coin]].sell = create_url_coinbase(coin_symbols[coin], 'sell')
        dict_of_coins[coin_names[coin]].purchase = create_url_coinbase(coin_symbols[coin], 'buy')

    print(dict_of_coins['Bitcoin'].sell, dict_of_coins['Bitcoin'].purchase)
    return(dict_of_coins)
coinbase()

def blockchain():
    """Purpose: To obtain selling and purchase price of inputted coins on blockchain
        Parameters: None
        Return Value: dict_of_coins = A dictionary whos keys are the names of the inputted coins
                    and values are CoinInfo objects containing name, symbol, sell, and purchase price
    """
    coin_symbols = ['BTC-USD', 'ETH-USD']
    coin_names = ['Bitcoin', 'Etherium']
    dict_of_coins = {}

    for coin in range(len(coin_symbols)):
        dict_of_coins[coin_names[coin]] = CoinInfo(coin_names[coin])
        dict_of_coins[coin_names[coin]].symbol = coin_symbols[coin]
        dict_of_coins[coin_names[coin]].sell, dict_of_coins[coin_names[coin]].purchase = create_url_blockchain(coin_symbols[coin])

    print(dict_of_coins['Bitcoin'].sell, dict_of_coins['Bitcoin'].purchase)
    return(dict_of_coins)
blockchain()


def find_best():
    dict_of_coins_blockchain = blockchain()
    dict_of_coins_coinbase = coinbase()
    #make a list and find the min and max of the coin

    # print(dict_of_coins_blockchain['BTC-USD'].sell, dict_of_coins_blockchain['BTC-USD'].purchase, dict_of_coins_blockchain['BTC-USD'].sell, dict_of_coins_blockchain['ETH-USD'].purchase)
    # print(dict_of_coins_coinbase['BTC-USD'].sell, dict_of_coins_coinbase['BTC-USD'].purchase, dict_of_coins_coinbase['ETH-USD'].sell, dict_of_coins_coinbase['ETH-USD'].purchase)
    #
    # print("The best source to sell Bitcoin is: ", max(float(dict_of_coins_blockchain['BTC-USD'].sell), float(dict_of_coins_coinbase['BTC-USD'].sell)))
    # print("The best source to purchase Bitcoin is: ", min(float(dict_of_coins_blockchain['BTC-USD'].purchase), float(dict_of_coins_coinbase['BTC-USD'].purchase)))
    #
    # print("The best source to sell Etherium is: ", max(float(dict_of_coins_blockchain['BTC-USD'].sell), float(dict_of_coins_coinbase['ETH-USD'].sell)))
    # print("The best source to purchase Etherium is: ", min(float(dict_of_coins_blockchain['BTC-USD'].purchase), float(dict_of_coins_coinbase['ETH-USD'].purchase)))
    print(dict_of_coins_blockchain)
    print(dict_of_coins_coinbase)

# find_best()
