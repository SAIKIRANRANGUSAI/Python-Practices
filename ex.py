from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "sai"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Sai@8978"
app.config["MYSQL_DB"] = "sai"

mysql = MySQL(app)

@app.route('/')
def home():
    print("MySQL Host:", app.config["MYSQL_HOST"])
    print("MySQL User:", app.config["MYSQL_USER"])
    print("MySQL Password:", app.config["MYSQL_PASSWORD"])
    print("MySQL Database:", app.config["MYSQL_DB"])
    print("MySQL Connection:", mysql.connection)

    if mysql.connection:
        print("MySQL connection established successfully")
        cur = mysql.connection.cursor()
        print("Cursor:", cur)  # Debug statement
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    else:
        print("MySQL connection is None")
        return "MySQL connection is None"

if __name__ == '__main__':
    app.run(debug=True)
