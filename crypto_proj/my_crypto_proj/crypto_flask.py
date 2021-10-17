from flask import Flask, request, jsonify, render_template
from crypto_logic import find_best, coinbase, blockchain

app = Flask(__name__)

@app.route("/coin_info", methods = ["GET"])
def check_coinbase_api():
    x = find_best(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    return(jsonify({'coin_info_buy': x,
                    # 'coin_info_sell': y
                    }))

@app.route("/weblook", methods = ["GET"])
def website_looker():
    coinbase_coins = coinbase(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    blockchain_coins = blockchain(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    best_buy_list, best_sell_list = find_best(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])

    return render_template('index.html', coinbase_coins = coinbase_coins, blockchain_coins = blockchain_coins,
                            best_buy_list = best_buy_list, best_sell_list = best_sell_list)

    # return render_template('index.html')

app.run(debug=True)
