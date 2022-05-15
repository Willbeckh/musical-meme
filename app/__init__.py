"""sets the main application factory"""
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    """method that sets the main application factory"""
    app = Flask(__name__)
    
    # app bluprints
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    # init flask ext
    db.init_app(app)
    
    # app configs
    app.config.from_object(config_options[config_name])
    
    return app