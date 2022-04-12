from flask import Blueprint, render_template
import requests

pokemon = Blueprint("pokemon", __name__)

#Main route with the function to print all pokemons names
@pokemon.route("/pokemon")
def index():
    return render_template("pokemons.html", title = "Pokemons")

#Just testing the api https://pokeapi.co
@pokemon.route("/pokemon/<pokemon>")
def test(pokemon):
    request = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
   
    request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
  
        
    if not request:
        return render_template("pokemons.html", title = pokemon)
    
    return render_template("pokemons.html", pokemon = request.json(), title = pokemon)
