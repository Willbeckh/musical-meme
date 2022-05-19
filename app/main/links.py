'''all application blueprints'''
from flask import Blueprint

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__, url_prefix='/authenticate')

from app.main import views
from app.auth import views