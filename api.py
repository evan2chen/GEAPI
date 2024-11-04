
from flask import Flask, jsonify, request
from explain import *
import random

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
    return "welcome to the mystery box have fun"

@app.route('/mystery_box/cube', methods = ['GET'])
def cube():
    from collections import defaultdict
    actions = ["north", "south", "east", "west", "up", "down"]
    freq = defaultdict(int)
    question = []
    for i in range (10):
        action = random.choice(actions)
        question.append(action)
        freq[action] += 1
    height =abs( freq["up"] - freq["down"])
    length = abs(freq["west"] - freq["east"])
    width = abs(freq["north"] - freq["south"])
    answer = (length+1)*(width+1)*(height+1)

    text = """
    A cube moves through 3D space in discrete units. 
    Calculate the volume of the rectangle described by the 
    start point and the end point as opposing corners of the rectangle.
    Avoid using external tools.
            
    """
    for d in question:
        text += f"{d}\n"

    text += f"\nAnswer: /spoiler {answer}"

    return text

@app.route('/mystery_box/hi', methods=['GET'])
def hi():
    randmsg = [
        "hi",
        "hello",
            
    ]
    return random.choice(randmsg)

@app.route('/mystery_box/help', methods=['GET'])
def help():

    randmsg = [
        "HELLLP HELLP!!! HELP MEE HELP HELP",
        "sorry cant help",
        "try doing $double all",
        "ill help if you ask one more time",
        "/tts lol"
    ]
    return random.choice(randmsg)

@app.route('/mystery_box/lol', methods=['GET'])
def lol():
    return "?"


if __name__ == '__main__':
    app.run(debug=True)
