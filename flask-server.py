from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    data = "Hello, world"
    return data

app.run("example.localhost", 8080)
