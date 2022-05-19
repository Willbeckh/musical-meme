from . import main
from flask import render_template, abort, redirect, url_for, request, flash, session
from jinja2 import TemplateNotFound

@main.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)