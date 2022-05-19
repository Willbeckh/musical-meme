import requests
import random
from flask import render_template, flash, redirect, url_for, abort
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


@main.route('/post/<int:post_id>')
# @login_required
def post(post_id):
    
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.all()
    form = CommentForm()
    return render_template('post.html', title=post.title, post=post,  comments=comments, form=form)


@main.route('/post/<int:post_id>/comment', methods=['GET', 'POST'])
# @login_required
def comment(post_id):
    """Method to enable a user to comment on a post"""
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment_text.data,
                          author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'info')
        return redirect(url_for('main.post', post_id=post_id))
    return render_template('comment.html', title="Comment", form=form)


@main.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
  post = Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash(f'Your post `Title: {post.title}` has been Deleted!', 'info')
  return redirect(url_for('main.index'))
