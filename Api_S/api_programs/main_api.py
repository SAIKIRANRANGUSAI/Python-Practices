from flask import Flask, json, jsonify
from data_api import read_all
app = Flask(__name__)

@app.route("/")
def sai():
    return jsonify(read_all())

if __name__ == '__main__':
    app.run(debug=True)