from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "saikiran"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_DB"] = "saikiran"
app.config["MYSQL_PASSWORD"] = "Sai@8978"

mysql = MySQL(app)

@app.route("/")
def sai():
    if mysql.connection:
        kiran = mysql.connection.cursor()
        kiran.execute("SELECT * FROM newinfo")
        rsk = kiran.fetchall()
        kiran.close()

        rangu = []

        for row in rsk:
            # Assuming the columns in the table are in order: Id, name, address, phonenumber, age
            formatted_row = {
                "Id": row[0],
                "name": row[1],
                "address": row[2],
                "phonenumber": row[3],
                "age": row[4]
            }
            rangu.append(formatted_row)

        return jsonify(rangu)
    else:
        print("Sorry, not connected")
        return "Not connected"

if __name__ == '__main__':
    app.run(debug=True)
