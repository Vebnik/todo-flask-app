from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevelopementConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints import
    from app.todo import todo
    from app.auth import auth

    app.register_blueprint(todo)
    app.register_blueprint(auth)
        
    return app
