from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from wtforms.validators import Email, EqualTo
from app.models import User


class NewPostForm(FlaskForm):
    """class that defines the add post form"""
    # title, text, submit
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text: ', validators=[Length(min=2, max=400)])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """class that defines the comment form"""
    comment_text = TextAreaField('Comment', validators=[
                                 Length(min=2, max=200)])
    submit = SubmitField('Submit')
