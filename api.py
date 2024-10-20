from flask import Flask, jsonify
import requests

app = Flask(__name__)



@app.route('/')
def empty():
    return jsonify({"message": "hello this is an empty page"})


@app.route('/valassistant/positioning',methods = ['GET'])
def positioning():
    map = requests.args.get('map', default = None).lower()
    gun = requests.args.get('weapon', default = None).lower()
    rank = requests.args.get('rank', default = None).lower()

    return f"You requested to see the positioning guide for {rank} players on {map} with {gun}"



@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({"message": "hi"})



if __name__ == '__main__':
    app.run(debug=True)
