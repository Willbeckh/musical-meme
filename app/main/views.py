import requests
import random
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app.main.links import main
from app.models import *
from app.main.forms import *


@main.route('/')
@main.route('/index')
def index():
    posts = Post.query.all()
    url = 'https://type.fit/api/quotes';
    response = requests.get(url)
    quotes_list = response.json()
    quotes = quotes_list[random.randint(0,1000)]
    return render_template('index.html', posts=posts, quote=quotes)



@main.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    """Method to enable a user to create a new post"""
    form = NewPostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, text=form.text.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!' , 'info')
        return redirect(url_for('main.index'))
    return render_template('add_post.html', title="Add post", form=form)
