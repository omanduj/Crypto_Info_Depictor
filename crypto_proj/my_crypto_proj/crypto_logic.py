import requests
import json

class CoinInfo():
    """Purpose: To crease an object to hold all info on coins
        Parameters: None
        Return Value: None
    """
    def __init__(self, name):
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
    coin_list = ['BTC-USD', 'ETH-USD']
    dict_of_coins = {}

    for coin in coin_list:
        dict_of_coins[coin] = CoinInfo(coin)
        dict_of_coins[coin].name = coin
        dict_of_coins[coin].sell = create_url_coinbase(coin, 'sell')
        dict_of_coins[coin].purchase = create_url_coinbase(coin, 'buy')

    return(dict_of_coins)

def blockchain():
    coin_list = ['BTC-USD', 'ETH-USD']

    #make another list with the names of the coins

    dict_of_coins = {}

    for coin in coin_list:
        dict_of_coins[coin] = CoinInfo(coin)
        dict_of_coins[coin].name = coin
        dict_of_coins[coin].sell, dict_of_coins[coin].purchase = create_url_blockchain(coin)

    return(dict_of_coins)


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

find_best()
