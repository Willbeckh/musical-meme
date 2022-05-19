from flask import render_template, abort, redirect, url_for, request, flash, session
from app.main.links import main
from app.models import *


@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)