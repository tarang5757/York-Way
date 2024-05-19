from flask import request, jsonify, render_template
from . import app, db

# default endpoint
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/navigate")
def navigate():
    return render_template("navigate.html")
