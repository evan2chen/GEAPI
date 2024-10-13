from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({"message": "hi"})

if __name__ == '__main__':
    app.run(debug=True)
