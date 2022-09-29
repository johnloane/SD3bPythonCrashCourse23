from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sport"):
        return render_template("failure.html")
    return render_template("success.html")

if __name__ == '__main__':
    app.run()


