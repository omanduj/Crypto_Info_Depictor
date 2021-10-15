from flask import Flask, request, jsonify
from crypto_logic import find_best

app = Flask(__name__)

@app.route("/coin_info", methods = ["GET"])
def check_coinbase_api():
    x, y = find_best(['BTC-USD', 'ETH-USD', 'DOGE-USD'], ['Bitcoin', 'Etherium', 'Dogecoin'])
    return(jsonify({'coin_info_buy': x,
                    'coin_info_sell': y
                    }))

app.run(debug=True)
