from flask import Flask, request, jsonify, render_template
from crypto_logic import find_best, coinbase, blockchain

app = Flask(__name__)

@app.route("/coin_info", methods = ["GET"])
def check_coinbase_api():
    optimal_coin_info = find_best(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    return(jsonify({'coin_info_buy': optimal_coin_info,
                    }))

@app.route("/webpage", methods = ["GET"])
def webpage():
    coinbase_coins = coinbase(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    blockchain_coins = blockchain(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    optimal_coin_info = find_best(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])

    return render_template('index.html', coinbase_coins = coinbase_coins, blockchain_coins = blockchain_coins,
                            optimal_coin_info = optimal_coin_info)

app.run(debug=True)
