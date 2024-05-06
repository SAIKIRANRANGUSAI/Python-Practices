from flask import Flask, jsonify, json

app = Flask(__name__)

data = {
    1:{
        "name":"kiran",
        "age":23
    },
    2:{
        "name":"sai",
        "age":24
    },
    3:{
        "name":"rangu",
        "age":25
    }
}

@app.route("/")
def sai():
    return jsonify(data)
@app.route("/<int:taskid>")
def kiran(taskid):
    if taskid in data:
        return jsonify(data[taskid])
    else:
        return jsonify({"error": "task not found"}),404


if __name__ == '__main__':
    app.run(debug=True)