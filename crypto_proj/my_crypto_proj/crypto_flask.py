from flask import Flask, request, jsonify
from crypto_logic import check_coinbase

app = Flask(__name__)

@app.route("/coin_info", methods = ["GET"])
def check_coinbase_api():
    x = check_coinbase()
    return(jsonify({'coin_info': x}))

app.run(debug=True)
