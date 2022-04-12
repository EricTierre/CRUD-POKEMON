from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
from routes.main import main
from routes.users import user
from routes.pokemon import pokemon

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(pokemon)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=12345, debug=True)
