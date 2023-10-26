from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/file")
def file():
    return render_template("index.html")


# main driver function
if __name__ == "__main__":
    app.run()
