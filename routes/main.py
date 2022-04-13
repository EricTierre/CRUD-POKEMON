from flask import Blueprint, redirect, render_template, session, url_for, request, flash
from extensions.database import mongo

main = Blueprint("main", __name__)

#Main route, HOME
@main.route("/")
def index():
    Collection_pokemons = mongo.db.pokemons

    pokemons = Collection_pokemons.find({})
    send_pokemons = []
    for i in pokemons:
        send_pokemons.append(i)
        
    if "username" in session:
        return render_template("crud.html", title = "CRUD", user = session["username"], pokemons = send_pokemons)
    else:
        return redirect(url_for("main.login"))

#Route use to login in the app
@main.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("main.index"))
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        userfound = mongo.db.users.find_one({"email" : email})

        if userfound:
            valid_user = userfound["email"]
            valid_password = userfound["password"]
            if valid_password == password:
                session["username"] = {"email": valid_user, "name": userfound["name"]}
                return redirect(url_for("main.index"))
            else:
                flash("wrong password")
                return render_template("login.html", title = "Login")
        else:
            flash("user not found")
            return render_template("login.html", title = "Login")
    else:
        return render_template("login.html", title = "Login")



#Route use to logout in the app
@main.route("/logout")
def logout():
    session.pop("username", None)
    flash("Good bye")
    return redirect(url_for("main.login"))
    

#Route use to register in the app
@main.route("/register", methods = ["GET", "POST"])
def register():
    if "username" in session:
        return redirect(url_for("main.index"))
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = {
            "name" : name,
            "email" : email,
            "password": password
        }

        #Check if the password have at least 8 characters
        if len(password) < 8:
            flash("Password must have at least 8 characters!")
            return redirect(url_for("main.register"))

        userfound = mongo.db.users.find_one({"email": email})
        #Check if the email already in the database
        if userfound:
            flash("Email already registered")
            return redirect(url_for("main.index"))
        else:
            Collection_Users = mongo.db.users
            Collection_Users.insert_one(user)
            flash("User registered!")
            return redirect(url_for("main.login"))
    else:
        return render_template("register.html", title = "Register")