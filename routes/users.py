from flask import Blueprint, render_template

user = Blueprint("user", __name__)

@user.route("/user")
def index():
    return "user here"
