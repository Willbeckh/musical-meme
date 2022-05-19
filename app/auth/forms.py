"""User authentication forms."""
import imp
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class RegisterForm(FlaskForm):
    """Register form."""
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    password_confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')