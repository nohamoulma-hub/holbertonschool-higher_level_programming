#!/usr/bin/python3
"""Simple Flask API to manage a collection of users."""

from flask import Flask, jsonify, request
# Flask pour créer l'application
# jsonify pour transformer un dictionnaire/liste Python en réponse JSON
# request pour accéder aux données envoyées par le client (utile pour le POST)
app = Flask(__name__)
# permet à Flask de savoir où se trouve ton fichier pour
# localiser d'éventuelles ressources.

# Stockage en mémoire des utilisateurs (dictionnaire vide pour le push)
users = {}


# cette fonction doit être exécutée quand quelqu'un accède à l'URL racine.
@app.route('/')
def home():
    """Route racine : message de bienvenue."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """Retourne la liste de tous les noms d'utilisateurs."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Indique que l'API fonctionne."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Retourne l'objet complet correspondant à un utilisateur donné."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Ajoute un nouvel utilisateur à partir des données JSON envoyées."""
    new_user = request.get_json(silent=True)

    if new_user is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
