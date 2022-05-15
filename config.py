from distutils.debug import DEBUG
import os


class Config:
    """This class sets the main application configuration settings"""
    pass


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