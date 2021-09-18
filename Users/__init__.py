from Users.users import users_blueprint


def init_app(app):
    app.register_blueprint(users_blueprint)