from flask import Blueprint, redirect, render_template, request, flash, url_for
import pandas as pd
from extensions.database import mongo
from .main import main
from bson.objectid import ObjectId

pokemon = Blueprint("pokemon", __name__)

#Main route with the function to print all pokemons names
@pokemon.route("/pokemon")
def index():
    return render_template("pokemons.html", title = "Pokemons")

@pokemon.route("/pokemon/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        Collection_pokemons = mongo.db.pokemons

        name = request.form.get("name")
        height = request.form.get("height")
        weight = request.form.get("weight")
        base_experience = request.form.get("base_experience")

        new_pokemon = {
            "name": name,
            "height": height,
            "weight": weight,
            "base_experience": base_experience
        }

        flash("Pokemon added")
        Collection_pokemons.insert_one(new_pokemon)
        return redirect(url_for("main.index")) 
    else:
        return redirect(url_for("main.index"))

@pokemon.route("/pokemon/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        Collection_pokemons = mongo.db.pokemons

        id = request.form.get("id")
        name = request.form.get("name")
        height = request.form.get("height")
        weight = request.form.get("weight")
        base_experience = request.form.get("base_experience")

        # Values to be updated.
        newvalues = { "$set": { 'name': name, 'height': height, 'weight': weight, 'base_experience': base_experience } }

        flash("Pokemon updated")
        Collection_pokemons.update_one({"_id": ObjectId(id)}, newvalues)
        return redirect(url_for("main.index")) 

    else:
        return redirect(url_for("main.index"))

@pokemon.route("/pokemon/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        Collection_pokemons = mongo.db.pokemons

        id = request.form.get("id")
    
        flash("Pokemon removed")
        Collection_pokemons.delete_one({"_id": ObjectId(id)})
        return redirect(url_for("main.index")) 
    else:
        return redirect(url_for("main.index"))

#Organize all de first generations pokemons with pandas https://pokeapi.co
# @pokemon.route("/pokemon/organize")
# def Organize():
#     #List to save all the pokemons
#     pokemons = [] 
#     pokemons_quantity = 10
#     #Requests to all the pokemons required
#     for i in range(1, pokemons_quantity):
#         request = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))
#         pokemons.append(request.json())

#     #Store all the pokemons in panda DataFrame
#     data = pd.DataFrame(pokemons)

#     Collection_Pokemon = mongo.db.pokemons
#     for i in range(0, pokemons_quantity-1):
#         #Only store a few attributes
#         pokemon = {
#             "name" : str(data.iloc[i]["name"]),
#             "height": str(data.iloc[i]["height"]),
#             "weight": str(data.iloc[i]["weight"]),
#             "base_experience" : str(data.iloc[i]["base_experience"])
#         }

#         Collection_Pokemon.insert_one(pokemon)
   

#     return render_template("pokemons.html", pokemon = data.iloc[0], title = "Pokemons")






















#Just testing the api https://pokeapi.co
# @pokemon.route("/pokemon/<pokemon>")
# def test(pokemon):
#     request = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
   
#     request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
  
        
#     if not request:
#         return render_template("pokemons.html", title = pokemon)
    
#     return render_template("pokemons.html", pokemon = request.json(), title = pokemon)
    





