import json

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_DB"] = "saikiran"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Sai@8978"
app.config["MYSQL_HOST"] = "127.0.0.1"

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def get_all_records():
    if mysql.connection:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM emptable")
        records = cursor.fetchall()
        cursor.close()
        formatted_records = []
        for row in records:
            formatted_row = {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "phonenumber": row[3]
            }
            formatted_records.append(formatted_row)
        return jsonify(formatted_records)


@app.route("/<int:id>",methods=["GET"])
def by_id(id):
    if mysql.connection:
        sai = mysql.connection.cursor()
        sai.execute("select * from emptable where id = %s",(id,))
        kiran = sai.fetchone()
        sai.close()
        if kiran:
            id_data = {
                "id":kiran[0],
                "name":kiran[1],
                "age":kiran[2],
                "phonenumber":kiran[3]
            }
            return jsonify(id_data)
        else:
            return jsonify({"error":"data not found"}),404


@app.route("/", methods=["POST"])
def create_record():
    if mysql.connection:
        cursor = mysql.connection.cursor()
        new_record = request.json
        cursor.execute("INSERT INTO emptable(name, age, phonenumber) VALUES(%s, %s, %s)",
                       (new_record["name"], new_record["age"], new_record["phonenumber"]))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Created new resource"}), 201


@app.route("/<int:id>", methods=["PUT"])
def update_record(id):
    if mysql.connection:
        cursor = mysql.connection.cursor()
        update_data = request.json
        cursor.execute("UPDATE emptable SET name = %s, age = %s, phonenumber = %s WHERE id = %s",
                       (update_data["name"], update_data["age"], update_data["phonenumber"], id))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Data is updated"}), 200

@app.route("/<int:id>", methods=["DELETE"])
def delete_record(id):
    if mysql.connection:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM emptable WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Successfully deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
