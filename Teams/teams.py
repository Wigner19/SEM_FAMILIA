from typing import Optional
from flask import Blueprint, render_template


from Database.db import mongo


teams_blueprint = Blueprint("teams_blueprint", __name__, template_folder="templates")


@teams_blueprint.route("/teams", methods=["GET"])
def find_teams():

    teams_list = []
    collection_teams = mongo.db.teams

    for teams in collection_teams.find():
        teams_list.append(teams["name"])

    return render_template("teams.html", list=teams_list)


@teams_blueprint.route("/teams/<name>/<imagem>", methods=["POST"])
def create_team(name, imagem):

    collection_teams = mongo.db.teams

    for nome in collection_teams.find():
        if nome["name"] == name and nome["image"] == imagem:
            return render_template("teams.html", error="Time já cadastrado!")

    teams = {
        "name": name,
        "image": imagem,
    }

    collection_teams.insert_one(teams)

    return render_template("teams.html")


@teams_blueprint.route("/teams/<name>", methods=["DELETE"])
def delete_team(name):

    collection_teams = mongo.db.teams

    collection_teams.find_one_and_delete({"name": name})

    return render_template("teams.html", error="Time deletado")


@teams_blueprint.route("/teams/<name>/<new_name>/<new_image>", methods=["PUT"])
def update_team(name, new_name, new_image):

    collection_teams = mongo.db.teams

    collection_teams.find_and_modify({"name": name}, {"name": new_name, "imagem": new_image})

    return render_template("teams.html", error="Time atualizado")
