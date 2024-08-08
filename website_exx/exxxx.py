from flask import Flask, request, render_template, flash, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "sai"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_DB"] = "saikiran"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Sai@8978"

mysql = MySQL(app)

def createing_table():
    with app.app_context():
        sai = mysql.connection.cursor()
        sai.execute("create table IF NOT EXISTS shop_data ("
                    "id int auto_increment primary key,"
                    "name varchar(190) not null,"
                    "age int,"
                    "phone_number bigint(12))")

createing_table()

@app.route("/")
def main():
    return render_template("demo.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    phone_number = request.form["phone_number"]
    sai = mysql.connection.cursor()
    sai.execute("INSERT INTO shop_data (name, age, phone_number) VALUES (%s, %s, %s)", (name, age, phone_number))
    mysql.connection.commit()
    sai.close()
    flash("Data added successfully", "success")
    return redirect(url_for("main"))




if __name__ == '__main__':
    app.run(debug=True)