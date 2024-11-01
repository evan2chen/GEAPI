
from flask import Flask, jsonify, request
from explain import *


app = Flask(__name__)

@app.route('/ping')
def ping():
    return "ping received"

@app.route('/')
def empty():
    return jsonify({"message": "hello this is an empty page"})


@app.route('/valassistant/positioning',methods = ['GET'])
def positioning():
    map = request.args.get('map', default = None)
    gun = request.args.get('weapon', default = None)
    rank = request.args.get('rank', default = None)
    if not map or not gun or not rank:
        return jsonify({"error": "Missing parameters"}), 400
    
    map = map.lower()
    gun = gun.lower()
    rank = rank.lower()

    return f"You requested to see the positioning guide for {rank} players on {map} with {gun}"

@app.route('/G-Explain', methods = ['POST'])
def explain():
    message = request.json.get('message', None)
    user = request.json.get('userID', None)

    if message is not None and message != "":
        return GEA_Chat.static_explain(message)
    
    return "send a message please"


@app.route('/mystery_box/', methods=['GET'])
def mysterybox():
    return jsonify({"message": "welcome to the mystery box have fun"})
@app.route('/mysterybox/hi', methods=['GET'])
def hi():
    return jsonify({"message": "hi"})

@app.route('/mystery_box/help', methods=['GET'])
def help():
    return jsonify({"message": "HELLLP HELLP!!! HELP MEE HELP HELP"})

@app.route('/mystery_box/lol', methods=['GET'])
def lol():
    return jsonify({"message": "?"})


if __name__ == '__main__':
    app.run(debug=True)
