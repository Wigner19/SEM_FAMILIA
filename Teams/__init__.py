from Teams.teams import teams_blueprint


def init_app(app):
    app.register_blueprint(teams_blueprint)