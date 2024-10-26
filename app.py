from flask import Flask, Blueprint
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = "login.signup"
login_manager.login_message = ""
 
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
            SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
            SQLALCHEMY_DATABASE_URI =f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}", 
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLAlCHEMT_ECHO = True, #sql언어를 로그에 출력
            WTF_CSRF_SECRET_KEY = 'AuwzyszU5sugKN7Ks6f'
            )     

    # SQLAlchemy와 앱을 연계
    db.init_app(app)
    # Migrate와 앱을 연계
    Migrate(app, db)
    #csrf와 앱을 연계
    csrf.init_app(app)

    #login_manager와 앱을 연계
    login_manager.init_app(app)

    # crud 앱 연결
    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # auth 앱 연결
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    #login 앱 연결
    from apps.login import views as login_views
    app.register_blueprint(login_views.login, url_prefix="/login")

    return app
