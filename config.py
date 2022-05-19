import os


class Config:
    """This class sets the main application configuration settings"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY=os.environ.get('SECRET_KEY') or '<insert_secret_key_here>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProdConfig(Config):
    """Production configuration."""
    DEBUG = False
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}