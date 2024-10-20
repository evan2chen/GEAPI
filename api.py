
from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/')
def empty():
    return jsonify({"message": "hello this is an empty page"})


@app.route('/valassistant/positioning',methods = ['GET'])
def positioning():
    map = request.args.get('map', default = None).lower()
    gun = request.args.get('weapon', default = None).lower()
    rank = request.args.get('rank', default = None).lower()
    if not map or not gun or not rank:
        return jsonify({"error": "Missing parameters"}), 400
    
    map = map.lower()
    gun = gun.lower()
    rank = rank.lower()

    return f"You requested to see the positioning guide for {rank} players on {map} with {gun}"



@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({"message": "hi"})



if __name__ == '__main__':
    app.run(debug=True)
