from flask import Flask, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "sai"

app.config["MYSQL_DB"] = "saikiran"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Sai@8978"
app.config["MYSQL_HOST"] = "127.0.0.1"

mysql = MySQL(app)


def create_table():
    with app.app_context():
        sai = mysql.connection.cursor()
        sai.execute("CREATE TABLE IF NOT EXISTS new_project ("
                    "id INT AUTO_INCREMENT PRIMARY KEY,"
                    "name VARCHAR(200),"
                    "age INT,"
                    "phonenumber BIGINT(13),"
                    "address VARCHAR(190)"
                    ")")
        mysql.connection.commit()
        sai.close()
        return redirect(url_for("insert_data"))
create_table()

@app.route("/insert")
def insert_data():
    if mysql.connection:
        ssai = mysql.connection.cursor()
        ssai.execute("INSERT INTO new_project (name, age, phonenumber, address) "
                     "VALUES ('saikiran', 23, 8978553778, 'hyd')")
        mysql.connection.commit()
        ssai.close()
        return "Data inserted successfully."
    else:
        return "There is a connection problem, sorry!"

if __name__ == '__main__':
    app.run(debug=True)
