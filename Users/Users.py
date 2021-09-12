from flask import render_template, Blueprint


users_blueprint = Blueprint("users_blueprint", __name__, template_folder="templates", static_folder="static")


@users_blueprint.route("/users")
def getUsers():
    return render_template("users.html")
