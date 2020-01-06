from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
# from flask import Session

from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
    # Session(app)
    csrf.init_app(app)


    # 待定
    # from redis import Redis
    # red = Redis(host="127.0.0.1", port=6379, db=1)
    # app.config["SESSION_TYPE"] = "redis"
    # app.config["SESSION_REDIS"] = Redis(host="127.0.0.1", port=6379, db=1)
    # Session(app)

    # red.set("kkk", "666")
    # print(re.get("kkk"))


