from flask import request, jsonify, render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from . import app, db, bcrypt
from .models import User, RegisterForm, LoginForm


# default endpoint
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


# logout route
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# Register Route
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        # create a new User and initialize username and password.
        new_user = User(username=form.username.data, password=hashed_password)
        # add it to the database
        db.session.add(new_user)
        # push changes.
        db.session.commit()
        # redirect to login page
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


# Need to work on this
@app.route("/navigate")
def navigate():
    return render_template("navigate.html")
