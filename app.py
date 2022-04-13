from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    #Session
    app.config["SECRET_KEY"] = "harrypotter"

    #Connect with the MongoDB
    app.config["MONGO_URI"] = "mongodb+srv://Eric:15975321@pokecrud.n8qha.mongodb.net/POKECRUD?retryWrites=true&w=majority"
    from extensions import database
    database.init_app(app)

    #Organize the routes
    from routes.main import main
    app.register_blueprint(main)
    
    from routes.users import user
    app.register_blueprint(user)

    from routes.pokemon import pokemon
    app.register_blueprint(pokemon)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=12345, debug=True)
