from flask import Flask, jsonify, request
from flask_cors import CORS
from GameLogic import Game
 
app = Flask(__name__)
CORS(app)
 
game = Game()


@app.route("/saldo", methods=["GET"])
def saldo():
    return jsonify({"saldo": game.saldo})