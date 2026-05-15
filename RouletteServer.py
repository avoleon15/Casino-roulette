from flask import Flask, jsonify, request
from flask_cors import CORS
from GameLogic import Game
 
app = Flask(__name__)
CORS(app)
 
game = Game()


@app.route("/saldo", methods=["GET"])
def saldo():
    return jsonify({"saldo": game.saldo})


@app.route("/apostar", methods=["POST"])
def apostar():
    data = request.get_json()
    number = data.get("number")
    color = data.get("color")
    monto = data.get("monto")
 
    if number is None or color is None or monto is None:
        return jsonify({"error": "Faltan campos: number, color, monto"}), 400
 
    exito = game.apostar(number, color, monto)
    if exito:
        return jsonify({"mensaje": "Apuesta registrada", "saldo": game.saldo})
    else:
        return jsonify({"error": "Saldo insuficiente o monto inválido"}), 400
    

@app.route("/ver_apuestas", methods=["GET"])
def ver_apuestas():
    apuestas = game.apuestas.ver_apuestas()
    return jsonify({"apuestas": apuestas})

@app.route("/girar" methods=["POST"])
def girar():
    if game.apuestas.size == 0:
        return jsonify({"apuestas": "No hay ninguna apuesta regresitada"}), 400
    
    numero_ganador = game.calcular_resultado()
    color_ganador = game._color_del_numero(numero_ganador)

    return jsonify({
        "numero ganador": numero_ganador,
        "color ganador": color_ganador,
        "saldo": game.saldo
    })