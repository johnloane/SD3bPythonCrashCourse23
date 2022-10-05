from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

SPORTS = ["Basketball", "Lawn Tennis", "Soccer", "Table Tennis", "Badminton"]

app = Flask(__name__)

app.config['MYSQL_HOST'] = '*****'
app.config['MYSQL_USER'] = '*****'
app.config['MYSQL_PASSWORD'] = '*****'
app.config['MYSQL_DB'] = '*****'

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", sports=SPORTS)
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Stop messing with my website")
    cursor = mysql.connection.cursor()
    cursor.execute("insert into registrants(name, sport) values (%s, %s)", (name, sport))
    mysql.connection.commit()
    cursor.close()
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    cur = mysql.connection.cursor()
    cur.execute("select * from registrants")
    result = cur.fetchall()
    return render_template("registrants.html", registrants=result)

if __name__ == '__main__':
    app.run()


