from flask import Flask 
from pathlib import Path # 경로 처리을 위한 라이브러리
from flask_migrate import Migrate
from apps.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config


# SQLAlchemy를 인스턴스화한다
db = SQLAlchemy()
# 해킹 방지
csrf = CSRFProtect()

# 이름이 정해짐
def create_app(config_key):
    app=Flask(__name__)

    app.config.from_object(config[config_key])
    # app.config.from_mapping(
    #     SECRET_KEY = "2dfawrasdfswJ",
    #     SQLALCHEMY_DATABASE_URI=
    #     f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
    #     SQLALCHEMY_TRACK_MOFIFICATIONS = False,
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_SECRET_KEY="Aasdfsdfq23zZf",
    # )

    csrf.init_app(app)
    
    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    
    # Migrate와 앱을 연계한다
    Migrate(app, db)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app