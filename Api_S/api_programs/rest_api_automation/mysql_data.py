from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = '127.0.0.1'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'Sai@8978'
app.config["MYSQL_DB"] = 'saikiran'

mysql = MySQL(app)

@app.route("/",methods=["GET"])
def getting():
    if mysql.connection:
        sai = mysql.connection.cursor()
        sai.execute("select * from emptable")
        kiran=sai.fetchall()
        sai.close()
        mysql_data = []
        for row in kiran:
            new = {
                "id":row[0],
                "name":row[1],
                "age":row[2],
                "phonenumber":row[3]
            }
            mysql_data.append(new)
        return jsonify(mysql_data)

@app.route("/<int:id>",methods=["GET"])
def by_id(id):
    if mysql.connection:
        sai = mysql.connection.cursor()
        sai.execute("select * from emptable where id = %s",(id,))
        kiran = sai.fetchone()
        sai.close()
        mysql_formate = {
            "id":kiran[0],
            "name":kiran[1],
            "age":kiran[2],
            "phonenumber":kiran[3]
        }
        return jsonify(mysql_formate)

@app.route("/p", methods=["POST"])
def posting():
    if mysql.connection:
        new_record = request.json
        name = new_record.get("name")
        age = new_record.get("age")
        phonenumber = new_record.get("phonenumber")
        sai = mysql.connection.cursor()
        sai.execute("INSERT INTO emptable (name, age, phonenumber) VALUES (%s, %s, %s)", (name, age, phonenumber))
        mysql.connection.commit()
        sai.close()
        return jsonify({"success": "Uploaded successfully"}), 201

@app.route("/pu/<int:id>",methods=["PUT"])
def putting(id):
    if mysql.connection:
        json_data = request.json
        name = json_data['name']
        age = json_data['age']
        phonenumber = json_data['phonenumber']
        sai = mysql.connection.cursor()
        sai.execute("update emptable set name=%s, age=%s, phonenumber=%s where id = %s",(name,age,phonenumber, id))
        mysql.connection.commit()
        sai.close()
        return jsonify({"success":"updated sucessfully"}), 200

@app.route("/d/<int:id>", methods=["DELETE"])
def deleting(id):
    if mysql.connection:
        sai = mysql.connection.cursor()
        sai.execute("DELETE FROM emptable WHERE id = %s", (id,))
        mysql.connection.commit()
        sai.close()
        return jsonify({"success": "deleted successfully"}), 200



if __name__ == '__main__':
    app.run(debug=True)