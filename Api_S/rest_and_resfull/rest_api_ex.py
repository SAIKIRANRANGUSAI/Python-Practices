from flask import Flask, jsonify, request


app = Flask(__name__)

data = [
    {"id": 1, "name": "sai"},
    {"id": 3, "name": "kiran"},
    {"id": 2, "name": "rangu"},
    {"id": 4, "name": "rsk"}
]


@app.route("/", methods=["GET"])
def main():
    return jsonify(data)

@app.route("/<int:id>", methods=["GET"])
def main2(id):
    sai = next((i for i in data if i["id"] == id), None)
    if sai is not None:
        return jsonify(sai)
    else:
        return jsonify({"error": "not found"}), 404

@app.route("/", methods=["POST"])
def posting():
    new = request.json
    data.append(new)
    return jsonify({"message": "created new resource"}), 201

@app.route("/", methods=["PUT"])
def putting():
    update = request.json
    for item in data:
        if item["id"] == update["id"]:
            item.update(update)
            return jsonify({"message": "data is updated"}), 200
    return jsonify({"error": "not found"}), 404

@app.route("/del/<int:id>",methods=["DELETE"])
def deleting(id):
    for item in data:
        if item["id"] == id:
            data.remove(item)
            return jsonify({"message": "sucesfully deleted"}), 204
    return jsonify({"error": "not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
