

# app/__init__.py

# third-party imports
from flask import abort, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import create_engine

#pymysql
import pymysql
import pandas as pd


# local imports
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://root:1234@127.0.0.1/dreamteam_db'
   
    
    # SECRET_KEY = 'p9Bv<3Eid9%$i01'
    
    
    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "Come on~ You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # Custom Error Pages

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    # To view the internal server error page
    @app.route('/500')
    def error():
        abort(500)

    # To deploy on heroku connection between pymysql and localhost
    def db_connector():
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='dreamteam_db', charset='utf8')
        cursor = db.cursor()
        sql = '''SELECT * FROM dreamteam_db.employees;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return str(result)
    
    @app.route('/')
    def index():
        a = db_connector()
        return a

    return app