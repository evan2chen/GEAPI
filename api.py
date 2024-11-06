
from flask import Flask, jsonify, request
from explain import *
import random

app = Flask(__name__)

@app.route('/ping', methods = ['POST'])
def ping():
    return "ping received from GEAPI"





@app.route('/val', methods = ['POST'])
@app.route('/valassistant',methods = ['POST'])
def positioning():
    pass
    return 'this is the val assistant endpoint, updates coming soon'

@app.route('/explain', methods = ['POST'])
def explain():
    message = request.message
    user = request.client

    if message is not None and message != "":
        return GEA_Chat.static_explain(message)
    
    return "send a message please"



@app.route('/mb', methods = ['POST'])
@app.route('/mystery_box/', methods=['POST'])
def mysterybox():
    return request.message








@app.route('/mystery_box/cube', methods = ['POST'])
def cube():
    from collections import defaultdict
    actions = ["North", "South", "East", "West", "Up", "Down"]
    freq = defaultdict(int)
    question = []
    for i in range (10):
        action = random.choice(actions)
        question.append(action)
        freq[action] += 1
    height =abs( freq["Up"] - freq["Down"])
    length = abs(freq["West"] - freq["East"])
    width = abs(freq["North"] - freq["South"])
    answer = (length+1)*(width+1)*(height+1)

    text = """A cube of volume 1 moves through 3D space in discrete units.\nCalculate the volume of the rectangle described by the\nstart point and the end point as opposing corners of the rectangle.\nAvoid using external tools.\n\n"""
    for d in question:
        text += f"{d}\n"

    text += f"\nAnswer: ||    {answer}   ||"

    return text


@app.route('/mystery_box/hi', methods=['POST'])
def hi():
    randmsg = [
        "hi",
        "hello",
            
    ]
    return random.choice(randmsg)

@app.route('/mystery_box/help', methods=['POST'])
def help():

    randmsg = [
        "HELLLP HELLP!!! HELP MEE HELP HELP",
        "sorry cant help",
        "try doing $double all",
        "ill help if you ask one more time",
        "lol"
    ]
    return random.choice(randmsg)

@app.route('/mystery_box/lol', methods=['POST'])
def lol():
    return "?"







@app.route('/')
def empty():
    return jsonify({"message": "hello this is an empty page"})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def catch_mystery_box(path):
    return f"{path}({request.method}) isn't a valid endpoint. add suggestions to $feedback if it should be a command", 404


if __name__ == '__main__':
    app.run(debug=True)
