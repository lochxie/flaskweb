from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return 'hello, flaskweb'

@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"hello {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)