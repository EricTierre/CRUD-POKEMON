from flask import Blueprint, render_template

main = Blueprint("main", __name__)

#Main route, HOME
@main.route("/")
def index():
    return render_template("crud.html", title = "1nfluencersmarketing - TEST")

#Route use to login in the app
@main.route("/login")
def login():
    return render_template("login.html", title = "Login")

#Route use to logout in the app
@main.route("/logout")
def logout():
    return "logout"

#Route use to register in the app
@main.route("/Register")
def register():
    return render_template("register.html", title = "Register")
