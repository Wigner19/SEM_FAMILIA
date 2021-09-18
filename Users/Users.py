from flask import render_template, Blueprint
from Database.db import mongo


users_blueprint = Blueprint("users_blueprint", __name__, template_folder="templates", static_folder="static")


@users_blueprint.route("/users", methods=["GET"])
def find_users():

    user_list = []
    collection_users = mongo.db.users

    for user in collection_users.find():
        user_list.append(user["name"])

    return render_template("users.html", list=user_list)


@users_blueprint.route("/users/<name>", methods=["POST"])
def create_users(name): 

    collection_users = mongo.db.users

    for nome in collection_users.find():
        if nome["name"] == name:
            return render_template("users.html", error="Nome já cadastrado!")

    user = {
        "name": name
    }

    collection_users.insert_one(user)

    return render_template("users.html")


@users_blueprint.route("/users/<name>", methods=["DELETE"])
def delete_user(name):

    collection_users = mongo.db.users

    collection_users.find_one_and_delete({"name": name})

    return render_template("users.html", error="Nome deletado")


@users_blueprint.route("/users/<name>/<newName>", methods=["PUT"])
def update_user(name, newName):

    collection_users = mongo.db.users

    collection_users.find_and_modify({"name": name}, {"name": newName})

    return render_template("users.html", error="Nome atualizado")
