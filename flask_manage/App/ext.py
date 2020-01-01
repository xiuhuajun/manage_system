from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
    # Session(app)
