import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = os.environ.get('SERVER_KEY')
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/typing")
def typing():
    return render_template("typing.html")


if __name__ == '__main__':
    app.run(debug=True)
