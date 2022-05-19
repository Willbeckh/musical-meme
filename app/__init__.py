"""sets the main application factory"""
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    """method that sets the main application factory"""
    app = Flask(__name__, instance_relative_config=True)
    
     # app settings.
    app.config.from_object(config_options[config_name])
        
     # init flask ext
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    
    # app blueprints
    from app.main.links import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
       
   
    return app