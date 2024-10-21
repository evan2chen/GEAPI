
from flask import Flask, jsonify, request
from explain import *


app = Flask(__name__)



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



@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({"message": "hi"})



if __name__ == '__main__':
    app.run(debug=True)
